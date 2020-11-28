
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import { Link } from "react-router-dom";


function PostDetail({match}) {

    const [post, setPost] = useState([])
    // const [category, setCategory] = useState([])
    const id = match.params.id

    useEffect(() => {
        axios({
            method: "GET",
            url: `http://127.0.0.1:8000/api/blogpost/${id}/`
        }).then(response => {
            setPost(response.data)
            // setCategory(response.data.blog_category)
        })
    }, [id])

  return (
    <div>
        Post with id {post.id}
        <p>Title: <strong>{post.title}</strong></p>
        <p>{post.content}</p>
        <hr />

        {/*<div className="row">*/}
        {/*    {posts.map(p => (*/}
        {/*        <div className="col-md-4" key={p.id}>*/}
        {/*            <h4>{p.title}</h4>*/}
        {/*            <p>{p.content}</p>*/}
        {/*            <p>{p.id}</p>*/}
        {/*            <Link to={{pathname: `/blogpost/${p.id}/`, fromDashboard: false}}>More....</Link>*/}
        {/*        </div>*/}
        {/*    ))}*/}

        {/*</div>*/}
    </div>
  );
}

export default PostDetail;
