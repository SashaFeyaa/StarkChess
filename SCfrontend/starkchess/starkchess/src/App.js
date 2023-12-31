import React, { useEffect, useState } from 'react';
import './App.css';
import { Routes, Route, BrowserRouter as Router } from 'react-router-dom';
import PvC from "./components/PvC";
import PvP from './components/PvP';
import Header from './components/Header';
import Footer from './components/Footer';
import About from './components/About';
import LoadingScreen from './components/LoadingScreen';

function App() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Після завантаження сторінки приховуємо анімацію
    setTimeout(() => {
      setLoading(false);
    }, 2000); // Штучна затримка для емуляції завантаження (можете видалити цю стрічку у реальному застосунку)
  }, []);

  return (
    <Router>
      <div className="app">
        <Header />
        {loading ? (
          <LoadingScreen />
        ) : (
          <main>
            <Routes>
              <Route path="/" element={<About />} />
              <Route path="/pvc" element={<PvC />} />
              <Route path="/pvp" element={<PvP />} />
            </Routes>
          </main>
        )}
        <Footer></Footer>
      </div>
    </Router>
  );
}

export default App;
