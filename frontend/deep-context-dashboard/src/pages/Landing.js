import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import SearchBar from '../components/ui/SearchBar';
import Button from '../components/ui/Button';
import Header from '../components/layout/Header';

const Landing = () => {
  const [url, setUrl] = useState('');
  const navigate = useNavigate();

  const handleSearch = () => {
    if (url) {
      navigate(`/dashboard?url=${encodeURIComponent(url)}`);
    }
  };

  return (
    <>
      <Header />
      <div className="flex flex-col items-center justify-center min-h-screen">
        <h1 className="text-5xl font-bold mb-8">Deep Context Sentiment Analysis</h1>
        <div className="w-full max-w-xl">
          <SearchBar value={url} onChange={(e) => setUrl(e.target.value)} />
          <Button onClick={handleSearch} className="mt-4">
            Analyze
          </Button>
        </div>
      </div>
    </>
  );
};

export default Landing;