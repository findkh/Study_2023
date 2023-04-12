package getAddress;

import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;

public class getAddr3 {

  public static void main(String[] args) {
    //모든 ip주소와 mac 주소를 배열에 저장
    try {
      Enumeration<NetworkInterface> interfaces = NetworkInterface.getNetworkInterfaces();
      List<String> ipAddresses = new ArrayList<>();
      List<String> macAddresses = new ArrayList<>();
      while (interfaces.hasMoreElements()) {
        NetworkInterface networkInterface = interfaces.nextElement();
        if (networkInterface.isUp()) {
          Enumeration<InetAddress> addresses = networkInterface.getInetAddresses();
          while (addresses.hasMoreElements()) {
            InetAddress address = addresses.nextElement();
            if (!address.isLinkLocalAddress() && !address.isLoopbackAddress() && address instanceof Inet4Address) {
              ipAddresses.add(address.getHostAddress());
            }
          }
          byte[] mac = networkInterface.getHardwareAddress();
          if (mac != null) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < mac.length; i++) {
              sb.append(String.format("%02X%s", mac[i], (i < mac.length - 1) ? "-" : ""));
            }
            macAddresses.add(sb.toString());
          }
        }
      }
      System.out.println("IP addresses: " + ipAddresses);
      System.out.println("MAC addresses: " + macAddresses);
    } catch (SocketException e) {
      throw new RuntimeException("Error getting network interface information", e);
    }

  }

}
