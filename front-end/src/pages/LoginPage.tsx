import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { Alert, Avatar, Box, Typography, Container } from '@mui/material';
import LoadingButton from '@mui/lab/LoadingButton';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import { CredentialResponse, GoogleLogin } from '@react-oauth/google';
import { useLogin } from 'src/hooks/auth';

// import { Copyright } from '../components/Copyright';
// import { useForm } from 'react-hook-form';
// import { validateEmail } from 'src/utils/validate-email';
// import { useLogin } from 'src/hooks/auth';
// import { Credentials } from 'src/types/credentials';
// import { ControlledTextField } from 'src/components/inputs/ControlledTextField';

export const LoginPage: React.FC = () => {

  const { mutateAsync: login, error: loginError, isLoading: isLoggingIn } = useLogin();
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogin = async (data: CredentialResponse) => {
    await login(data);

    type RedirectState = { from: string } | undefined;
    const redirectedFrom = (location.state as RedirectState)?.from;
    if (redirectedFrom) {
      navigate(redirectedFrom);
    } else {
      navigate('/dash');
    }
  };

  return (
    <Container component="main" maxWidth="xs">
      <Typography component="h1" variant="h2" align="center" sx={{ mt: 8 }}>
        Scuffed circus
      </Typography>
      <Box
        sx={{
          mt: 4,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        {/* <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
          <LockOutlinedIcon />
        </Avatar> */}
       <Box>
        <GoogleLogin
              onSuccess={handleLogin}
              onError={() => {
                console.log('Login Failed');
              }}
            
            />
       </Box>
      </Box>
      {/* <Copyright /> */}
    </Container>
  );
};
