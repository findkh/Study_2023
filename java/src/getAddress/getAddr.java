package getAddress;

import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.net.UnknownHostException;

public class getAddr {
  public static void main(String[] args) {
    try {
      // 로컬 호스트의 IP 주소를 얻음
      InetAddress localHost = InetAddress.getLocalHost();
      System.out.println("IP 주소: " + localHost.getHostAddress());

      // 로컬 호스트의 네트워크 인터페이스를 얻음
      NetworkInterface networkInterface = NetworkInterface.getByInetAddress(localHost);

      // 네트워크 인터페이스가 null이 아니라면 MAC 주소를 얻음
      if (networkInterface != null) {
        byte[] macAddress = networkInterface.getHardwareAddress();
        if (macAddress != null) {
          StringBuilder sb = new StringBuilder();
          for (int i = 0; i < macAddress.length; i++) {
            sb.append(String.format("%02X%s", macAddress[i], (i < macAddress.length - 1) ? "-" : ""));
          }
          System.out.println("MAC 주소: " + sb.toString());
        } else {
          System.out.println("MAC 주소를 찾을 수 없습니다.");
        }
      } else {
        System.out.println("네트워크 인터페이스를 찾을 수 없습니다.");
      }
    } catch (UnknownHostException | SocketException e) {
      e.printStackTrace();
    }
  }
}
