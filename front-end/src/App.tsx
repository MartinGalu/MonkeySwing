import React from 'react';
import { BrowserRouter, Routes, Route, Navigate, Outlet, useLocation } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import { QueryClientProvider } from 'react-query';
import { Box, CircularProgress, CssBaseline } from '@mui/material';

import { queryClient } from './config';
import { DashPage } from './components/DashPage';
import { theme } from './theme';
import { PageNotFound404 } from './components/PageNotFound404';
import { ConfirmProvider } from 'material-ui-confirm';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
import { LocalizationProvider } from '@mui/x-date-pickers';
import { HomePage } from './pages/HomePage';
import { CompPage } from './pages/CompPage';
import { LoginPage } from './pages/LoginPage';
import { useGetMe } from './hooks/auth';

const App: React.FC = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <CssBaseline />
        <ThemeProvider theme={theme}>
          <ConfirmProvider>
            <BrowserRouter>
              <Routes>
                <Route element={<ProtectedPage />}>
                  <Route path="/dash" element={<DashPage />}>
                    <Route index element={<HomePage />} />
                    <Route path="profit/*" element={<CompPage />} />
                  </Route>
                </Route>
                <Route path="/login" element={<LoginPage />} />
                <Route index element={<Index />} />
                <Route path="*" element={<PageNotFound404 />} />
              </Routes>
            </BrowserRouter>
          </ConfirmProvider>
        </ThemeProvider>
      </LocalizationProvider>
    </QueryClientProvider>
  );
};

const MainPage: React.FC = () => {
  return <Outlet />;
};

const Index: React.FC = () => {
  return <Navigate to="/login" replace />;
};

const Progress: React.FC = () => {
  return (
    <Box sx={{ display: 'grid', placeContent: 'center', height: '100vh' }}>
      <CircularProgress />
    </Box>
  );
};

const ProtectedPage: React.FC = () => {
  const location = useLocation();
  const { status } = useGetMe();
  if (status === 'error') {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }
  if (status === 'loading') {
    return <Progress />;
  }

  return <Outlet />;
};

export default App;
