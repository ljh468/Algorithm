package 해쉬;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * S문자열에서 T문자열과 아나그램이 되는 S의 부분문자열의 개수를 구하는 프로그램을 작성
 * 아나그램 판별시 대소문자가 구분됩니다. 부분문자열은 연속된 문자열이어야 함
 *
 * 입력
 * bacaAacba
 * abc
 *
 * 출력
 * 3
 *
 */
public class _04_모든_아나그램_찾기 {

  public int solution1(String s, String t) {
    int answer = 0;

    // 1. 찾아야 할 아나그램 초기값 setting
    Map<Character, Integer> map1 = new HashMap<>();
    for (char x : t.toCharArray()) {
      map1.put(x, map1.getOrDefault(x, 0) + 1);
    }

    // 2. 투포인터를 이용해서 검증할 map을 생성
    Map<Character, Integer> map2 = new HashMap<>();
    char[] arr = s.toCharArray();
    int lt = 0;

    // 3. rt 이동
    for (int rt = 0; rt < arr.length; rt++) {
      map2.put(s.charAt(rt), map2.getOrDefault(s.charAt(rt), 0) + 1);

      // 슬라이딩 윈도우가 완성되면, 아나그램인지 확인
      if (rt - lt + 1 == t.length()) {
        if (map1.equals(map2)) {
          answer++;
        }

        // 4. lt 이동
        map2.put(s.charAt(lt), map2.get(s.charAt(lt)) - 1);

        // lt가 0이 되면 map에서 제거
        if (map2.get(s.charAt(lt)) == 0) {
          map2.remove(s.charAt(lt));
        }
        lt++;

      }
    }
    return answer;
  }

  public static void main(String[] args) {
    _04_모든_아나그램_찾기 t = new _04_모든_아나그램_찾기();
    Scanner sc = new Scanner(System.in);
    String S = sc.next();
    String T = sc.next();
    System.out.println(t.solution1(S, T));
  }
}
