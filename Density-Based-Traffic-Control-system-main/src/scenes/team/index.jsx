import { Box, Typography, useTheme } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { tokens } from "../../theme";
import { trafficData } from "../../data/traffic_data";
import AdminPanelSettingsOutlinedIcon from "@mui/icons-material/AdminPanelSettingsOutlined";
import LockOpenOutlinedIcon from "@mui/icons-material/LockOpenOutlined";
import SecurityOutlinedIcon from "@mui/icons-material/SecurityOutlined";
import Header from "../../components/Header";

const Team = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const columns = [
    { field: "ID",
     headerName: "ID",
     },
    {
      field: "Timestamp",
      headerName: "Timestamp",
    },
    {
      field: "road1",
      headerName: "Lane 1",
      
    },
    {
      field: "road2",
      headerName: "Lane 2",
      
    },
    
    {
      field: "road3",
      headerName: "Lane 3",
      
    },
    {
      field: "road4",
      headerName: "Lane 4",
      
    },
    {
      field: "open",
      headerName: "Open Lane",
      flex: 1
      },
  ];

  return (
    <Box m="20px">
      <Header title="Records" subtitle="Fetched using AWS-IOT" />
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
        }}
      >
        <DataGrid checkboxSelection rows={trafficData} columns={columns} getRowId={row => row.ID}/>
      </Box>
    </Box>
  );
};

export default Team;
