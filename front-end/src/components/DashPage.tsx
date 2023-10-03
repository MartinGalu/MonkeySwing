import React, { useState } from 'react';
import { Outlet, useNavigate } from 'react-router-dom';
import useMediaQuery from '@mui/material/useMediaQuery';
import Box from '@mui/material/Box';
import Navigation from './Navigation';
import { theme } from 'src/theme';
import { logout } from 'src/api/auth';
import { ListItemIcon, Menu, MenuItem, MenuProps } from '@mui/material';
import { LogoutOutlined } from '@mui/icons-material';

export interface DashPageOutletContext {
  handleDrawerToggle(): void;
}

const drawerWidth = 256;

export const DashPage: React.FC = () => {
  const [mobileOpen, setMobileOpen] = useState(false);
  const isSmUp = useMediaQuery(theme.breakpoints.up('sm'));

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  const outletContext: DashPageOutletContext = { handleDrawerToggle };

  return (
    <Box sx={{ display: 'flex', minHeight: '100vh' }}>
      <Box component="nav" sx={{ width: { sm: drawerWidth }, flexShrink: { sm: 0 } }}>
        {isSmUp ? null : (
          <Navigation
            PaperProps={{ style: { width: drawerWidth } }}
            variant="temporary"
            open={mobileOpen}
            onClose={handleDrawerToggle}
          />
        )}
        <Navigation
          PaperProps={{ style: { width: drawerWidth } }}
          sx={{ display: { sm: 'block', xs: 'none' } }}
        />
      </Box>
      <Box
        sx={{
          flex: 1,
          display: 'flex',
          flexDirection: 'column',
          bgcolor: '#eaeff1',
          width: isSmUp ? `calc(100% - ${drawerWidth}px)` : '100%',
        }}
      >
        <Outlet context={outletContext} />
        <Box component="footer" sx={{ p: 2 }}>
          {/* <Copyright /> */}
        </Box>
      </Box>
    </Box>
  );
};
