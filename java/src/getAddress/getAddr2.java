package getAddress;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetAddress;

public class getAddr2 {
  public static void main(String[] args) throws Exception {
    // ipconfig/all 실행
    //    try {
    //      // Run ipconfig/all command
    //      Process process = Runtime.getRuntime().exec("ipconfig /all");
    //      BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
    //
    //      // Print output
    //      String line;
    //      while ((line = reader.readLine()) != null) {
    //        System.out.println(line);
    //      }
    //    } catch (IOException e) {
    //      e.printStackTrace();
    //    }

    try {
      //ip주소 가져오기
      InetAddress inetAddress = InetAddress.getLocalHost();
      String ipAddress = inetAddress.getHostAddress();
      System.out.println("IP Address: " + ipAddress);

      // 실행할 명령어 준비
      // getmac /fo csv /nh 명령어는 현재 사용 가능한 네트워크 어댑터의 MAC 주소를 CSV 형식으로 출력하되, 
      // 열 제목을 제외한 나머지 열만 표시하는 명령어
      String command = "getmac /fo csv /nh";

      // 명령어 실행 후 결과를 읽어옴
      Process process = Runtime.getRuntime().exec(command);
      BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
      String line = reader.readLine();

      // 결과에서 MAC 주소 추출
      String[] values = line.split(",");
      String macAddress = values[0].replace("\"", "");

      //MAC 주소 검증 코드
      String macPattern = "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$";
      if (macAddress.matches(macPattern)) {
        System.out.println("Valid MAC Address: " + macAddress);
      } else {
        System.out.println("Invalid MAC Address: " + macAddress);
      }

      // MAC 주소 출력
      System.out.println("MAC Address: " + macAddress);
    } catch (IOException e) {
      e.printStackTrace();
    } catch (NullPointerException e) {
      System.out.println("Unable to retrieve MAC address");
    }
  }
}