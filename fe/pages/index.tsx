import Head from 'next/head'
import { FC } from 'react';
import styles from '../styles/index.module.css';
const Home:FC =  function Home() {
  return (
    <div className="container">
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <h1>Upload new File</h1>
    <form method='post' encType='multipart/form-data'>
      <input type='file' name='file'/>
      <input type='submit' value='Upload' />
    </form>
    </div>
  )
}


export default Home;
