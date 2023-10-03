import { Typography } from '@mui/material';
import { Box } from '@mui/system';
import React from 'react';
import { DashPageHeader } from 'src/components/DashPageHeader';
import { useGetMe } from 'src/hooks/auth';

export const HomePage: React.FC = () => {
  const { data: user } = useGetMe();

  return (
    <>
      <DashPageHeader pageTitle="Home" />
      <Box component="main" sx={{ flex: 1, py: 6, px: 4, bgcolor: '#eaeff1' }}>
         <Typography variant="h5">Welcome {user?.name}!</Typography>
      </Box>
    </>
  );
};
