import './App.css';
import { useState } from 'react';
import axios from 'axios';
import styled from 'styled-components';
import 'bootstrap/dist/css/bootstrap.min.css';
import Alert from 'react-bootstrap/Alert'

function App() {
  const [showSuccess, setShowSuccess] = useState(false);
  const [showError, setShowError] = useState(false);
  const [secondsLeft, setSecondsLeft] = useState(0);
  const [message, setMessage] = useState('');
  const [token, setToken] = useState(0);
  const [username, setUsername] = useState(0);

  const getToken = () => {
    axios.get('http://127.0.0.1:8000/generar_token?cliente=jorge.ayala')
    .then(res => {
      setShowSuccess(true)
      setShowError(false)
      setMessage(res.data.message)
      setSecondsLeft(res.data.secondsLeft)
      setToken(res.data.token)
      setUsername(res.data.username)

    })
    .catch(error => {
      setShowError(true)
      setShowSuccess(false)
      setMessage('El servicio no está disponible por el momento')
    })
  }

  return (
    <div>
      <GeneralContainer>
        <GetTokenButton onClick={getToken}>Usar token virtual</GetTokenButton>
      </GeneralContainer>
      {showError ? <Alert variant="danger">
        <Alert.Heading>¡Error!</Alert.Heading>
        <p>
        {message}
        </p>
      </Alert> : null}
      {showSuccess ? <Alert variant="success">
        <Alert.Heading>{token ? <p>TOKEN: {token}</p> : null}</Alert.Heading>
        {username ? <p>Usuario: {username}</p> : null}
        {secondsLeft ? <p>Expira luego de {secondsLeft} segundos</p> : null}
        <hr />
        {message ? <p className="mb-0">{message}</p> : null}
      </Alert> : null}
    </div>
  );
  
}

const GetTokenButton = styled.button`
	display: block;
	padding: 10px 30px;
	border-radius: 100px;
	color: #fff;
	border: none;
	background: #1766DC;
	cursor: pointer;
	font-family: 'Roboto', sans-serif;
	font-weight: 500;
	transition: .3s ease all;
	&:hover {
		background: #0066FF;
	}
`;


const GeneralContainer = styled.div`
	padding: 40px;
	display: flex;
	flex-wrap: wrap;
	justify-content: center;
	gap: 20px;
`;


export default App;
