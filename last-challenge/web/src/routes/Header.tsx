import { useForm } from "react-hook-form";
import { Link, useLocation } from "react-router-dom";
import { styled } from "styled-components";

const Container = styled.div`
    display: flex;
    height: 40px;
    padding: 4px;
`;

const Logo = styled.div`
    width: 30px;
    height: 30px;
    background-image: url("https://www.ntoworks.com/img/logo.svg");
    background-size: cover;
`;

const Status = styled.div`
    display: flex;
    height: 40px;
    
    /* background-color: cyan; */
    flex-direction: column;
    align-items: center;
    margin-left: 10px;
    margin-top: 8px;
    p:first-child {
        width: 100%;
        font-size: 8px;
        color: white;
        text-align: left;
    }
    p:last-child {
        width: 100%;
        font-size: 10px;
        color: white;
        text-align: left;

    }
`;

const FormContainer = styled.div`
    position: absolute;
    right: 0px;
    justify-content: end;
    align-items: end;    
`;

const Form = styled.form`
    display: flex;
    flex-direction: column;
    position: absolute;
    right: 0px;

    input {
        border: none;
        margin: 2px;
        border-radius: 2px;
        background-color: rgba(255, 255, 255, 0.7);
        text-align: center;

        &::placeholder {
            color: rgba(0, 0, 0, 0.65);
            font-size: 10px;
            text-align: center;
        }
    }

    span {
        font-size: 8px;
        color: rgba(255, 0, 0, 0.9);
        font-weight: bold;
        padding-bottom: 4px;
    }

`;

interface IForm {
    keyword: string;
}

const Header = () => {
    const { register, handleSubmit, formState: {errors} } = useForm<IForm>();
    const location = useLocation();
    const { password } = location.state || {};
    console.log(password);

    const doSearch = (data: IForm) => {
        console.log(data.keyword);
    }
    
    return <Container>
        <Link to={"/"} ><Logo /></Link>
        <Status>
            {/* <p>2023년 11월 20일 오후 11:20</p>
            <p>python으로 검색된 결과 입니다.</p> */}
        </Status>
        <Form onSubmit={handleSubmit(doSearch)}> 
            <input {...register("keyword", {
                required: "검색할 키워드를 입력하세요.",
                minLength: {
                    value: 2,
                    message: "키워드는 두글자 이상 입력해야 합니다."
                }
            })} placeholder="키워드를 입력하세요" />
            <span>{errors?.keyword?.message}</span>    
        </Form>
            
    </Container>
}

export default Header;