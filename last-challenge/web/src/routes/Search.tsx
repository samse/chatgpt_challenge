import { useLocation, useParams } from "react-router-dom";
import { IJob, fetchWWRJobs, fetchROKJobs } from "../api/jobs-api";
import { useQuery } from "react-query";
import Header from "./Header";
import { styled } from "styled-components";
import { useEffect } from "react";
import { motion } from "framer-motion";


export const Container = styled.div`
    display: flex;
    justify-content: center;
    width: 100%;
`;

const Grid = styled.div`
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  width: 50vw;
  gap: 10px;
  margin-top: 50px;
`;

const Box = styled(motion.div)`
    display: flex;
    position: relative;
    min-height: 60px;
    margin: auto 0;
    width: 100%;
    gap: 10px; /* 그리드 간격 */
    justify-content: center;
    align-items: center;
    border-radius: 4px;
    background-color: rgba(255, 255, 255, 0.5);
    box-shadow:
        0 2px 3px rgba(0, 0, 0, 0.1),
        0 10px 20px rgba(0, 0, 0, 0.06);
    cursor: grab;

    p {
        position: absolute;
        top: 10px;
        font-size: 10px;
        width: 100%;
        text-align: left;
        padding-left: 10px;
    }

    h1 {
        width: 100%;
        padding-left: 10px;
        text-align: left;
        position: absolute;
        top: 20px;
        font-size: 10px;
    }
`;


export const Loading = styled.span`
  display: block;
  text-align: center;
  /* transform: rotateZ('360') 1s linear infinite; */
`;
let queryOnce = true;
const Search = () => {
    const location = useLocation();
    const { type } = location.state || {};
    const { keyword } = useParams();

    const { data, isLoading } = useQuery<IJob[]>(["fetch-jobs", keyword],
        () => type == "wwr" ? fetchWWRJobs(keyword ?? "") : fetchROKJobs(keyword ?? ""),
        { enabled: queryOnce });

    useEffect(() => {
        queryOnce = false;
    }, []);

    const onItemClick = (link: string) => {
        // 외부 브라우저 실행
        window.open(link);
    }

    return <Container>
        <Header />
        {isLoading ? <Loading>Loading...</Loading> : 
            <Grid>
                {data!.map((v: IJob) =>
                    <Box onClick={() => onItemClick(v.link)}>
                        <p>{v.title} {v.position}</p>
                    </Box>)}
            </Grid>}
    </Container>
}

export default Search;