import { Box } from "@mui/material";
import Header from "../../components/Header";
import BarChart from "../../components/HourlyBarChart";

const Bar = () => {
  return (
    <Box m="20px">
      <Header title="Bar Chart Hourly" subtitle="Simple Bar Chart" />
      <Box height="75vh">
        <BarChart />
      </Box>
    </Box>
  );
};

export default Bar;
