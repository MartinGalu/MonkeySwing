import React from 'react';
import { Box } from '@mui/material';
import { Route, Routes } from 'react-router-dom';
import { DashPageHeader } from 'src/components/DashPageHeader';
import { CompPageGenerator } from './CalculatorPage.GenerateProfit';

export const CompPage: React.FC = () => {
  return (
    <>
      <DashPageHeader
        pageTitle="Comp for this week"
      />
      <Box component="main" sx={{ flex: 1, py: 6, px: 4, bgcolor: '#eaeff1' }}>
        <Routes>
          <Route path="/" element={<CompPageGenerator />} />
          <Route path="*" element={'Whoops, no page here.'} />
        </Routes>
      </Box>
    </>
  );
};
