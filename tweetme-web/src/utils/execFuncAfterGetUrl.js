export default function execFuncAfterGetUrl(url, callback, is_json=true){
    const xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.onload = ()=>{
        console.log(xhr.response);
        let data = is_json ? JSON.parse(xhr.response) : xhr.response;
        callback(data);
    }
    xhr.send();
}