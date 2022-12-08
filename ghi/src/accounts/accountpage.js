import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
// import Link from '@mui/material/Link';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useAuthContext } from "./auth";
import { Link } from 'react-router-dom';
import CardsComponent from './card'



const cards = [1];



export default function AccountPageComponent(props) {
  const theme = createTheme();
  const { token } = useAuthContext()
  // const playlist = get_all_playlists()

  // for (each user in db)
  //   for each playlist in user
  //     playlist.name


  if (token) {
    return (
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <AppBar position="relative">
          <Toolbar>
            <Typography variant="h6" color="inherit" noWrap>
              <Link to="/"><img className="header-img" src="https://i.imgur.com/HxIEBd3.png" /></Link>
            </Typography>
          </Toolbar>
        </AppBar>
        <main>
          {/* Hero unit */}
          <Box
            sx={{
              bgcolor: 'background.paper',
              pt: 8,
              pb: 6,
            }}
          >
            <Container maxWidth="sm">
              <Typography
                component="h1"
                variant="h3"
                align="center"
                color="text.primary"
                gutterBottom
              >
                😎 Here's your jams 😎
              </Typography>
              <Typography variant="h5" align="center" color="text.secondary" paragraph>
              </Typography>
              <Stack
                sx={{ pt: 4 }}
                direction="row"
                spacing={2}
                justifyContent="center"
              >
                <Button className="recs-btn" variant="outlined" text_decoration="none"><Link to="/music/recommendations">Create a new Jam</Link></Button>
              </Stack>
            </Container>
          </Box>
          <Container sx={{ py: 8 }} maxWidth="md">
            {/* End hero unit */}
            <Grid container spacing={4}>
              {cards.map((card) => (
                <Grid item key={card} xs={12} sm={6} md={4}>
                  {/* for card in cards? */}
                  {/* {CardsComponent} */}
                </Grid>
              ))}
            </Grid>
          </Container>
        </main>
        {/* Footer */}
        <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
          <Typography variant="h6" align="center" gutterBottom>
            Footer
          </Typography>
          <Typography
            variant="subtitle1"
            align="center"
            color="text.secondary"
            component="p"
          >
            JamPackd - Created 2022 by Marble, Zoybh, Joyce & Tiffany
          </Typography>
        </Box>
        {/* End footer */}
      </ThemeProvider >
    );
  }
}