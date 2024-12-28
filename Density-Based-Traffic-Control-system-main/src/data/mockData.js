import { tokens } from "../theme";
import {mockTransactions} from "./traffic_data"
import { trafficData } from "./traffic_data";
console.log("mockTransactions", mockTransactions);

const openSumsByDate= trafficData.reduce((acc, item) => {
 const Timestamp = item.Timestamp.slice(0, 10);
  const open = item.open;

  if (!acc[Timestamp]) {
    acc[Timestamp] = { lane1: 0, lane2: 0, lane3: 0, lane4: 0 };
  }
  switch (open) {
    case 1:
      acc[Timestamp].lane1 += 1;
      break;
    case 2:
      acc[Timestamp].lane2 += 1;
      break;
    case 3:
      acc[Timestamp].lane3 += 1;
      break;
    case 4:
      acc[Timestamp].lane4 += 1;
      break;
    default:
      break;
  }

  return acc;
}, {});

export const mockBarData = [
  // iterate through the openSumsByDate object and create an array of objects that has the following shape:
  // {
  //   Timestamp: "2020-01-01",
  //   lane1: 0,
  //   lane2: 0,
  //   lane3: 0,
  //   lane4: 0
  // }

  ...Object.keys(openSumsByDate).map((key) => ({
    Timestamp: key,
    lane1: openSumsByDate[key].lane1,
    lane2: openSumsByDate[key].lane2,
    lane3: openSumsByDate[key].lane3,
    lane4: openSumsByDate[key].lane4
  }))
];

const openSumsByTimestamp= trafficData.reduce((acc, item) => {
  // use the hour time in Timestamp as the key for the accumulator object
  const Timestamp = item.Timestamp.slice(11, 13);
  const open = item.open;
 
   if (!acc[Timestamp]) {
     acc[Timestamp] = { lane1: 0, lane2: 0, lane3: 0, lane4: 0 };
   }
   switch (open) {
     case 1:
       acc[Timestamp].lane1 += 1;
       break;
     case 2:
       acc[Timestamp].lane2 += 1;
       break;
     case 3:
       acc[Timestamp].lane3 += 1;
       break;
     case 4:
       acc[Timestamp].lane4 += 1;
       break;
     default:
       break;
   }
 
   return acc;
 }, {});

export const mockHourlyData = [
  // iterate through the opensumsbyTimestamp object and create an array of objects that has the following shape:
  // {
  //   Timestamp: "HH",
  //   lane1: 0,
  //   lane2: 0,
  //   lane3: 0,
  //   lane4: 0
  // }
  ...Object.keys(openSumsByTimestamp).map((key) => ({
    Timestamp: key,
    lane1: openSumsByTimestamp[key].lane1,
    lane2: openSumsByTimestamp[key].lane2,
    lane3: openSumsByTimestamp[key].lane3,
    lane4: openSumsByTimestamp[key].lane4
  }))
]

export const mockLineData = [
  {
    id: "road1",
    color: "red",
    data: mockTransactions.map((item) => ({
      x: item.Timestamp,
      y: item.road1
    }))
  },
  {
    id: "road2",
    color: "blue",
    data: mockTransactions.map((item) => ({
      x: item.Timestamp,
      y: item.road2
    }))
  },
  {
    id: "road3",
    color: "green",
    data: mockTransactions.map((item) => ({
      x: item.Timestamp,
      y: item.road3
    }))
  },
  {
    id: "road4",
    color: "orange",
    data: mockTransactions.map((item) => ({
      x: item.Timestamp,
      y: item.road4
    }))
  },
];
