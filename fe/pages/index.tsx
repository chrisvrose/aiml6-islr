import Head from 'next/head';
// import 'bootstrap/dist/css/bootstrap.min.css';
import { Alert, Button, Col, Form, Row, Container } from 'react-bootstrap';
import { FC, FormEvent, useState } from 'react';
import styles from '../styles/index.module.css';
import { arrayBufferToBase64 } from '../etc/etc';
import { Header } from '../etc/Header';
import { Details } from '../etc/Details';
const Home: FC = function Home() {
    const [errorState, setErrorState] = useState<string | undefined>(undefined);
    const [imgData, setImgData] = useState<{ img: string; res: [string, string, string] } | undefined>(undefined);
    const onSub = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        console.log(e);
        const tg = e.target as any;
        // (window as any).tg = tg;
        if (tg.file.files.length === 0) {
            setErrorState('no files');
            setImgData(undefined);
            return;
        }
        const file = tg.file.files[0];
        const reader = new FileReader();

        reader.readAsArrayBuffer(file);
        reader.onload = async k => {
            // console.log(arrayBufferToBase64(reader.result));
            try {
                const fc = arrayBufferToBase64(reader.result);
                const rawResponse = await fetch('/upload', {
                    method: 'POST',
                    headers: {
                        Accept: 'application/json',
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ file: fc }),
                });
                const content = await rawResponse.json();
                console.log(content);
                if (content.ok === true && Array.isArray(content.res)) {
                    new Blob([reader.result as ArrayBuffer]);
                    console.log('content', content);
                    setImgData({ img: URL.createObjectURL(file), res: content.res });
                }
            } catch (e) {
                setErrorState('Error uploading file!');
                setImgData(undefined);
            }
            console.log('k');
        };
        reader.onerror = k => {
            setErrorState('Error loading file!');
        };
        reader.onabort = k => {
            setErrorState('Loading Aborted!');
        };
    };
    return (
        <>
            <Header />
            <Container fluid='md' style={{ paddingTop: '4.5rem' }}>
                <Row>
                    <Col md={{ span: 6, offset: 3 }}>
                        <Container fluid style={{ textAlign: 'center' }}>
                            <h2>Upload Image</h2>
                        </Container>
                        <Head>
                            <title>Create Next App</title>
                        </Head>

                        <Form onSubmit={onSub}>
                            {/* <input type='file' name='file' /> */}
                            <Form.Group controlId='formFile' className='mb-3'>
                                <Form.Label>Upload file</Form.Label>
                                <Form.Control type='file' name='file' />
                            </Form.Group>
                            <Button variant='primary' type='submit'>
                                Submit
                            </Button>
                            {/* <input type='submit' value='Upload' /> */}
                        </Form>
                        <Alert
                            variant='danger'
                            show={errorState !== undefined}
                            dismissible
                            onClose={() => setErrorState(undefined)}
                            className='spacer-top-margin'
                        >
                            <Alert.Heading>Error</Alert.Heading>
                            {errorState}
                        </Alert>
                    </Col>
                </Row>

                <Row>
                    <Col md={{ span: 6, offset: 3 }}>
                        <Container fluid style={{ textAlign: 'center' }}>
                            <h2>Results</h2>
                            {imgData?.img && <img style={{ width: '75%' }} src={imgData.img}></img>}
                            {imgData?.res && <Details deets={imgData.res} />}

                            <br />
                            {(errorState !== undefined || imgData !== undefined) && (
                                <Button
                                    onClick={() => {
                                        setErrorState(undefined);
                                        setImgData(undefined);
                                    }}
                                >
                                    Reset
                                </Button>
                            )}
                        </Container>
                    </Col>
                </Row>
            </Container>
        </>
    );
};

export default Home;
