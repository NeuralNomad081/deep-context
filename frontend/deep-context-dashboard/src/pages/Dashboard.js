import React, { useState, useEffect, useRef } from 'react';
import { useLocation } from 'react-router-dom';
import { getAnalysis } from '../services/api';
import SkeletonLoader from '../components/layout/SkeletonLoader';
import PostPreview from '../components/dashboard/PostPreview';
import SentimentCharts from '../components/dashboard/SentimentCharts';
import TopComments from '../components/dashboard/TopComments';
import AllComments from '../components/dashboard/AllComments';
import Header from '../components/layout/Header';

const Dashboard = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const location = useLocation();
  const fetchInitiated = useRef(false);

  useEffect(() => {
    const url = new URLSearchParams(location.search).get('url');
    if (url && !fetchInitiated.current) {
      fetchInitiated.current = true;
      getAnalysis(url)
        .then((response) => {
          // Check for the new 'summary' field to validate the response
          if (response.data && response.data.summary) {
            setData(response.data);
          } else {
            setError('Received invalid data structure from the server.');
          }
          setLoading(false);
        })
        .catch((err) => {
          console.error('Error fetching analysis:', err);
          setError('Failed to fetch analysis. Check the URL or console for details.');
          setLoading(false);
        });
    }
  }, [location.search]);

  if (loading) return <SkeletonLoader />;

  if (error) {
    return (
      <div className="flex items-center justify-center min-h-screen text-center">
        <div className="bg-red-900 border border-red-400 text-red-100 px-6 py-4 rounded-lg">
          <strong className="font-bold text-xl">An Error Occurred</strong>
          <p className="block mt-2">{error}</p>
        </div>
      </div>
    );
  }

  return (
    <>
      <Header />
      <div className="p-8">
        {data && (
          <div className="space-y-8">
            <div className="grid grid-cols-1 lg:grid-cols-5 gap-8">
               <div className="lg:col-span-2">
                 {/* FIX: Pass postUrl as a separate prop */}
                 <PostPreview
                   postContext={data.postContext}
                   postUrl={data.postUrl}
                 />
               </div>
               <div className="lg:col-span-3">
                 <SentimentCharts summary={data.summary} />
               </div>
             </div>

            {/* --- MIDDLE ROW: Top Comments now uses the full width --- */}
            <div>
              <TopComments topComments={data.topComments} />
            </div>

            {/* --- BOTTOM ROW: All Comments table --- */}
            <div>
              <AllComments topComments={data.topComments} />
            </div>
          </div>
        )}
      </div>
    </>
  );
};

export default Dashboard;