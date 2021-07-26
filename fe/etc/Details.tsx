import { FC } from 'react';
import { Table } from 'react-bootstrap';

const dat = ['SVM','7-KNN','G-NBC'] as const;

function Majority([x,y,z]:[string,string,string]){
    if(x===y||x===z){return x}
    else if(y===z) return y;
    else return y
}

export const Details: FC<{ deets: [string, string, string] }> = function (props) {
    const {deets} = props
    return (
        <>
            <Table striped bordered hover style={{marginTop:'2rem'}}>
                <thead>
                    <tr>
                        <th>Type</th>
                        <th>Classification</th>
                    </tr>
                </thead>
                <tbody>
                    {deets.map((e,i)=>{
                        return (<tr><td>{dat[i]}</td><td>{deets[i]}</td></tr>)
                    })}
                    <tr>
                        <td>Majority(FallBack KNN)</td>
                        <td>{Majority(deets)}</td>
                    </tr>
                    
                </tbody>
            </Table>
        </>
    );
};
