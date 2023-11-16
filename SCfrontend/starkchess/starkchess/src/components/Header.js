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

  const [walletName, setWalletName] = useState("");

  function handleConnect() {
    return async () => {
      const res = await connect();
      console.log(res);
      setWalletName(res?.name || "");
    };
  }

  function handleDisconnect() {
    return async () => {
      await disconnect();
      setWalletName("");
    };
  }

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
          <Button onClick={() => handleConnect()} className="connect__btn" color="inherit">
            CONNECT
          </Button>
          {walletName && (
              <div>
                <h2>
                  Selected Wallet: <pre>{walletName}</pre>
                </h2>
              </div>
            )}
        </Grid>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
