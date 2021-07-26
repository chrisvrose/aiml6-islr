import { AppProps } from 'next/app';
import '../styles/globals.css';
import Head from 'next/head';
function MyApp({ Component, pageProps }: AppProps) {
    return (
        <>
            <Head>
                <link
                        rel='stylesheet'
                        href='https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'
                    />
            </Head>
            <Component {...pageProps} />
        </>
    );
}

export default MyApp;
