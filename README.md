# Lidar-SLAM

1. Slam Toolbox installieren

  ```bash
  sudo apt update
  sudo apt install ros-humble-slam-toolbox
  ```
2. Workspace anlegen

  ```bash
  mkdir -p ~/<workspacename>/src
  ```

3. Treiber für Slamtec Lidar installieren

  ```bash
  cd ~/<workspacename>/src/
  git clone -b ros2 https://github.com/Slamtec/rplidar_ros.git
  ```

  ```bash
  cd ~/<workspacename>/
  source /opt/ros/humble/setup.bash
  colcon build --symlink-install
  ```

  ```bash
  source ./install/setup.bash
  ```  

  ```bash
  echo "source <workspacename>/install/setup.bash" >> ~/.bashrc
  source ~/.bashrc
  ```

  ```bash
  cd ~/<workspacename>/src/rpldiar_ros/
  source scripts/create_udev_rules.sh
  ```

4. 

  ```bash
  cd ~/<workspacename>/src/
  git clone -b ros2 https://
