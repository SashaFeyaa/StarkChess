import ReactReact, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import '../styles/Header.css';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import Brightness4Icon from '@mui/icons-material/Brightness4';
import {
  connect,
  disconnect,
} from "get-starknet"

const Header = () => {

  const [provider, setProvider] = useState('')
  const [address, setAddress] = useState('')
  const [name, setName] = useState('')
  const [inputAddress, setInputAddress] = useState('')
  const [retrievedName, setRetrievedName] = useState('')
  const [isConnected, setIsConnected] = useState(false)

  const connectWallet = async() => {
    try{
      // let the user choose a starknet wallet
      const starknet = await connect()
      // connect to the user-chosen wallet
      await starknet?.enable({ starknetVersion: "v4" })
      // set account provider
      setProvider(starknet.account)
      // set user address
      setAddress(starknet.selectedAddress)
      // set connection status
      setIsConnected(true)
    }
    catch(error){
      alert(error.message)
    }
  }

  // persist state on reload
  useEffect(() => {
      connectWallet()
  }, [])

  return (
    <AppBar position='relative' className='header'>
      <Toolbar className='header__content'>
        <Typography variant="h6" component="div">
          <Link to="/">
            <img src="/imgbg/logo/starkchess.png" alt="Logo" />
          </Link>
        </Typography>
        <div className="pages">
          <Button className="pages__btn" color="inherit">
            <Link to="/">ABOUT</Link>
          </Button>
          <Button className="pages__btn" color="inherit">
            <Link to="/leaderboard">LEADERBOARD</Link>
          </Button>
          <Button className="pages__btn" color="inherit">
            <Link to="/pvp">PvP</Link>
          </Button>
          <Button className="pages__btn" color="inherit">
            <Link to="/pvc">PvC</Link>
          </Button>
          <Button className="pages__btn" color="inherit">
            <Link to="/profile">PROFILE</Link>
          </Button>
        </div>
        <Grid className="connect" container>
        {
            isConnected ?
            <Button className="connect__btn" color="inherit">{address.slice(0, 5)}...{address.slice(60)}</Button> :
            <Button className="connect__btn" color="inherit" onClick={() => connectWallet()}>Connect wallet</Button>
          }
        </Grid>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
