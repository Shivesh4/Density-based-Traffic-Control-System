#include <Arduino.h>
#include <algorithm>
#include <map>
#include <vector>
#include <string>

// Define global variables
int road1, road2, road3, road4;
int min_order[4][2];
int min_order_index[4];
int open_signal;
unsigned long timer; // Use unsigned long for millis() to handle longer durations

// Additional variable declarations
std::map<std::string, unsigned long> signal_open_time;
std::vector<int> previous_signal;


void signalCalc() {
  for (int i = 0; i < 4; i++) {
    if (checkOthers(min_order_index[i]) && timer <= 0) {
      open_signal = min_order_index[i];
      timer = 30000; // Set timer to 30 seconds (30,000 milliseconds)
    }
  }
}

// Sort the values of the roads
void sortRoadValues() {
  int temp[4] = {road1, road2, road3, road4};

  // Sort the temporary array and update min_order and min_order_index
  std::pair<int, int> tempOrder[4];
  for (int i = 0; i < 4; i++) {
    tempOrder[i] = std::make_pair(i + 1, temp[i]);
  }
  std::sort(tempOrder, tempOrder + 4, [](const auto& a, const auto& b) {
    return a.second < b.second;
  });

  for (int i = 0; i < 4; i++) {
    min_order[i][0] = tempOrder[i].first;
    min_order[i][1] = tempOrder[i].second;
    min_order_index[i] = tempOrder[i].first;
  }
}



bool checkOthers(int curr) {
  if (min_order[0][0] == curr) { // Check if the current signal is the lowest
    if (previous_signal.back() == curr) { // curr is the current open signal
      for (const auto& i : min_order) {
        if (i[1] <= 18 && i[0] != curr) {
          return false;
        }
      }
      return true;
    } else { // curr is not the current open signal
      if (std::find(previous_signal.end() - 2, previous_signal.end(), curr) != previous_signal.end()) {
        for (const auto& i : min_order) {
          if (i[1] <= 18 && i[0] != curr && i[0] != open_signal) {
            return false;
          }
        }
      }
      return true;
    }
  } else {
    if (previous_signal.back() == curr) { // curr is not the current open signal
      for (const auto& i : min_order) {
        if (i[1] <= 18 && i[0] != curr) {
          return false;
        }
      }
      return true;
    } else { // curr is not the current open signal
      if (std::find(previous_signal.end() - 2, previous_signal.end(), curr) != previous_signal.end()) {
        for (const auto& i : min_order) {
          if (i[1] <= 18 && i[0] != curr && i[0] != open_signal) {
            return false;
          }
        }
      }
      return true;
    }
  }
}

void handle_signal_change(int current) {
  unsigned long current_id = millis();
  static unsigned long extra_timer = 0;

  timer -= 1;
  extra_timer += 1;

  if (current == previous_signal.back()) {
    if (extra_timer >= 30) {
      extra_timer = 0;
      previous_signal.push_back(current);
    }
    return;
  } else {
    extra_timer = 0;
    signal_open_time["signal"] = current;
    signal_open_time["start_time"] = current_id;
    previous_signal.push_back(current);
  }
}

std::map<std::string, int> message_generate(const std::string& timestamp) {
  static unsigned long current_id = 0;
  sortRoadValues();
  handle_signal_change(open_signal);

  int minute = std::stoi(timestamp.substr(14, 2));
  int hour = std::stoi(timestamp.substr(11, 2));
  int day = std::stoi(timestamp.substr(8, 2)) % 7;

  std::map<std::string, int> message = {
    {"ID", static_cast<int>(current_id)},
    {"open", open_signal},
    {"road1", road1},
    {"road2", road2},
    {"road3", road3},
    {"road4", road4},
    {"Minute", minute},
    {"Hour", hour},
    {"Day", day}
  };

  current_id += 1;
  return message;
}
