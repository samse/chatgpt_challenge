import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { styled } from "styled-components";

const Container = styled.div`
    display: flex;
    flex-direction: column;
    height: 100vh;
    justify-content: center;
    align-items: center;
`;

const Form = styled.form`
    display: flex;
    justify-content: center;
    align-items: center;

    input {
        border: none;
        margin: 2px;
        padding: 6px;
        
        border-radius: 2px;
        background-color: rgba(255, 255, 255, 0.7);
        text-align: center;

        &::placeholder {
            color: rgba(0, 0, 0, 0.65);
            font-size: 10px;
            text-align: center;
        }
    }

    button {
        border-color: rgba(255, 255, 255, 0.8);
        border-radius: 4px;
        background-color: rgba(255, 255, 255, 0.5);
        border: none;
        padding: 6px 30px;
        margin: 10px;
    }

    span {
        font-size: 8px;
        color: rgba(255, 0, 0, 0.9);
        font-weight: bold;
        padding-bottom: 4px;
    }

    label {
        font-size: 12px;       
        padding-right: 10px;
        color: rgba(255, 255, 255, 0.8);
    }
`;

const Title = styled.div`
    display: flex;
    position: absolute;
    top: 0px;
    margin: 10px;
    align-items: center;

    h1 {
        font-size: 12px;
        color: rgb(255, 255, 255, 0.9);
        top: 10px;
    }

    img {
        border-radius: 4px;
    }
`;

const Copyright = styled.h1`
    width: 100%;
    position: absolute;
    bottom: 0px;
    font-size: 10px;
    color: rgba(255, 255, 255, 0.7);
    text-align: center
`;

interface IForm {
    keyword: string
}

const Home = () => {
    const { register, handleSubmit, formState: {errors} } = useForm<IForm>();
    const { register: register2, handleSubmit: handleSubmit2, formState: {errors: errors2} } = useForm<IForm>();
    const navigate = useNavigate();
    
    const doWWRSearch = (data: IForm) => {
        console.log("valid", data);
        //window.location.href=`./jobs/search/keyword=${data.keyword}`
        navigate(`/search/${data.keyword}`, { state: {type: "wwr"}})
    }
    const doROKSearch = (data: IForm) => {
        console.log("valid", data);
        //window.location.href=`./jobs/search/keyword=${data.keyword}`
        navigate(`/search/${data.keyword}`, { state: {type: "rok"}})
    }

    return <>
        <Title><h1>구직자 검색</h1></Title>
        <Container>
            <Form key="wwr" onSubmit={handleSubmit(doWWRSearch)}>
                <label>RemoteOK 에서 </label>
                <input {...register("keyword", {
                    required: "검색할 키워드를 입력하세요.",
                    minLength: {
                        value: 2,
                        message: "키워드는 두글자 이상 입력하세요"
                    }
                }
                )} placeholder="검색어를 입력하세요" />
                <span>{errors?.keyword?.message}</span>
                <button>검 색</button>
            </Form>
            <Form key="rok" onSubmit={handleSubmit2(doWWRSearch)}>
                <label>Wework remotely 에서 </label>
                <input {...register2("keyword", {
                    required: "검색할 키워드를 입력하세요.",
                    minLength: {
                        value: 2,
                        message: "키워드는 두글자 이상 입력하세요"
                    }
                }
                )} placeholder="검색어를 입력하세요" />
                <span>{errors2?.keyword?.message}</span>
                <button>검 색</button>
            </Form>
        </Container>
        <Copyright>Copyright 2019, ntoworks company All rights reserved.</Copyright>
    </>
}

export default Home;