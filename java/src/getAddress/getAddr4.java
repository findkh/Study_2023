package getAddress;

import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class getAddr4 {
  public static void main(String[] args) {
    try {
      List<String> ipAddresses = new ArrayList<>();
      List<String> macAddresses = new ArrayList<>();
      // 모든 네트워크 인터페이스 정보 가져오기
      for (NetworkInterface ni : Collections.list(NetworkInterface.getNetworkInterfaces())) {
        // IP 주소와 맥 주소 가져오기
        for (InetAddress address : Collections.list(ni.getInetAddresses())) {
          // IPv4 주소인지 확인
          if (!address.isLinkLocalAddress() && !address.isLoopbackAddress() && address.getHostAddress().indexOf(':') < 0) {
            String ipAddress = address.getHostAddress();
            ipAddresses.add(ipAddress);
          }
        }
        byte[] mac = ni.getHardwareAddress();
        if (mac != null) {
          StringBuilder sb = new StringBuilder();
          for (byte b : mac) {
            sb.append(String.format("%02X", b));
            sb.append(":");
          }
          if (sb.length() > 0) {
            sb.deleteCharAt(sb.length() - 1);
          }
          String macAddress = sb.toString();
          macAddresses.add(macAddress);
        }
      }
      // IP 주소와 맥 주소 문자열 출력
      String ipAddressString = "'" + String.join("', '", ipAddresses) + "'";
      String macAddressString = "'" + String.join("', '", macAddresses) + "'";
      System.out.println("IP addresses: " + ipAddressString);
      System.out.println("MAC addresses: " + macAddressString);
    } catch (SocketException e) {
      e.printStackTrace();
    }
  }
}
