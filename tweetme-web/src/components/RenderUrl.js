import React, { useEffect, useState, useRef } from 'react'
import execFuncAfterGetUrl from '../utils/execFuncAfterGetUrl'
import ReactDOM from 'react-dom';


export default function RenderUrl({ url }) {
    const urlDivRef = useRef()
    useEffect(() => {
        urlDivRef.current.innerHTML = "NAMASHTE !!!"
        execFuncAfterGetUrl(url, (data)=>{
            ReactDOM.render(<p>{JSON.stringify(data)}</p>, urlDivRef.current)
        })
    }, [])
    return ( 
    <>
        <div ref={urlDivRef}></div>
    </>
    )
}