
const BASE_URL = "http://www.ntoworks.com:5001";

export interface IJob {
    title: string,
    position: string,
    link: string
}

export const fetchWWRJobs = (keyword: string) => {
    const url = `${BASE_URL}/wwr/?keyword=${keyword}`;
    console.log(`fetchWWRJobs => ${url}`);
    return fetch(url).then(response => {
        console.log("response: ", response);
        if (!response.ok) {
            throw new Error(`Network error : ${response.status}`);
        }
        const json = response.json()
        console.log("json: ", json);
        return json;
    });
}

export const fetchROKJobs = (keyword: string) => {
    const url = `${BASE_URL}/rok/?keyword=${keyword}`;
    console.log(`fetchROKJobs => ${url}`);
    return fetch(url).then(response => {
        console.log("response: ", response);
        if (!response.ok) {
            throw new Error(`Network error : ${response.status}`);
        }
        const json = response.json()
        console.log("json: ", json);
        return json;
    });
}
