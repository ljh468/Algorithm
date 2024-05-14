#include <bits/stdc++.h>
using namespace std;

int main(){
    // //////////////////////////////////////////////////////////////////////
    // /**
    //  * 메모리
    //  * 컴퓨터 메모리는 메모리 셀의 연속과 같으며 각 셀의 크기는 1바이트
    //  * 메모리 주소는 16진수로 표기되고 C++에서는
    //  * &연산자(ampersand)를 통해 변수의 메모리 주소를 얻을 수 있음
    //  * 변수에 값을 할당해도 메모리 주소는 변하지 않는다.
    //  */
    // //////////////////////////////////////////////////////////////////////
    // int i;
    // cout << &i << '\n';
    // i = 0;
    // cout << &i << '\n';

    // //////////////////////////////////////////////////////////////////////
    // /**
    //  * 포인터
    //  * C, C++은 개발자가 직접 필요한 메모리를 예약하고 해제할 수 있으며 포인터를 지원함
    //  * 변수의 메모리 주소를 담는 타입을 포인터라고 함
    //  * 포인터는 메모리 동적할당, 데이터를 복사하지 않고 함수 매개변수로 사용,
    //  * 클래스 및 구조체를 연결할 때 사용, *는 에스터리스크(asterisk operator)
    //  * 
    //  * ex) 연결리스트의 노드
    //  * class Node{
    //  * public:
    //  *     int data;
    //  *     Node* next;
    //  * }
    //  * 
    //  * 포인터의 크기는 OS가 32bit면 4byte, 64bit면 8byte
    //  */
    // //////////////////////////////////////////////////////////////////////
    // int i = 0;
    // string s = "jaehoon";

    // int *a = &i; // i의 메모리 주소값을 담음
    // cout << a << '\n';
    
    // string *b = &s; // s의 메모리 주소값을 담음
    // cout << b << '\n';

    // //////////////////////////////////////////////////////////////////////
    // /**
    //  * 역참조 연산자
    //  * C++에서 * 기호는 3가지 용도로 사용됨
    //  * 1. 이항 연산자에서 곱셈 연산으로
    //  * 2. 포인터 타입의 선언
    //  * 3. 역참조(dereference)로 메모리를 기반으로 변수의 값에 접근할때도 사용됨
    //  */
    // //////////////////////////////////////////////////////////////////////
    // string a = "abcda";
    // string *b = &a;
    // cout << b << "\n"; // 메모리 주소값
    // cout << *b << "\n"; // 역참조 연산자 (메모리에 있는 실제값)

    // //////////////////////////////////////////////////////////////////////
    // /**
    //  * array to pointer decay (배열에서 포인터 부식)
    //  * 배열의 이름을 주소값으로 쓸 수 있음 (int a[] -> a - 주소값)
    //  * 배열의 이름을 T* 포인터에 할당하면 T[N]이란 배열의 크기정보 N이 없어지고 첫번째 요소의 주소가 바인딩됨
    //  * 참고로 vector는 불가능, array만 가능
    //  */
    // //////////////////////////////////////////////////////////////////////
    // int a[3] = {1, 2, 3};
    // int *c = a; // a 첫번째 메모리 주소값만 들어감
    // cout << c << '\n';
    // cout << &a[0] << '\n';

    // cout << c+1 << '\n';
    // cout << &a[1] << '\n';

    // //////////////////////////////////////////////////////////////////////
    // /**
    //  * 이터레이터(iterator) - **각 컨테이너의 주소를 가리키틑 개체**
    //  * 이터레이터는 컨테이너에 저장되어 있는 요소의 주소를 가리키는 개체를 말하며 포인터를 추상화한 것
    //  * vector, map등 다르게 구현된 컨테이너들을 이터레이터를 통해 쉽게 순회할 수 있다.
    //  * 다만 주소값을 바로 반환하지는 못하며 &*를 통해 한단계 더 거쳐서 가리키는 해당 요소의 주소값을 반환할 수 있다.
    //  */
    // //////////////////////////////////////////////////////////////////////
    // vector<int> v;
    // for(int i = 1; i <= 5; i++){
    //     v.push_back(i);
    // }

    // // begin(), end()는 주소값 or 값을 바로 출력할 수 없음
    // cout << (*v.begin()) << "\n";
    // cout << (*v.end()) << "\n";

    // for(int i = 0; i < 5; i++){
    //     cout << i << "번째 요소 : " << *(v.begin() + i) << "\n";
    //     cout << &*(v.begin() + i) << "\n"; // &*를 이용해서 메모리 주소값에 접근
    // }
    // // auto로 vector<int>::iterator를 생략가능
    // for(auto it = v.begin(); it != v.end(); it++){
    //     cout << *it << ' ';
    // }
    // cout << '\n';
    // for(vector<int>::iterator it = v.begin(); it != v.end(); it++){
    //     cout << *it << ' ';
    // }
    // auto it = v.begin();
    // advance(it, 3); // 주어진 반복자를 지정된 수만큼 전진 (0부터 이동 -> 그러므로 4번째 4출력)
    // cout << '\n';
    // cout << *it << '\n';

    // //////////////////////////////////////////////////////////////////////
    // /**
    //  * 컨테이너의 메서드
    //  * begin()
    //  * - 컨테이너의 시작 위치를 반환
    //  * 
    //  * end()
    //  * - 컨테이너의 끝 다음의 위치를 반환, 실제 끝값의 다음을 가리키기때문에 어떤 요소도 가리키지 않음
    //  * - for(auto it = v.begin(); it != v.end(); ++it){} 이런식으로 활용
    //  * 
    //  * advance(iterator, count)
    //  * - 해당 iterator를 count까지 증가 시킴 (0부터)
    //  */
    // //////////////////////////////////////////////////////////////////////

    // //////////////////////////////////////////////////////////////////////
    // /**
    //  * Q. 이터레이터와 포인터의 차이
    //  * 이터레이터는 어떠한 컨테이너(배열, 맵 등)의 범위안에서 일부 요소를 가리키며
    //  * 해당 요소들을 순회할 수 있는 개체
    //  * 반면 포인터는 변수의 메모리 주소를 저장하는 개체이며 포인터는 delete를 통해 포인터를 제거할 수 있음
    //  * 
    //  * Q. 이터레이터 = 일반화 포인터?
    //  * 일반화(generalization)는 공통된 속성들을 일반적인 개면으로 추상화한 형태를 말함
    //  * 이터레이터는 컨테이너에 저장된 각각의 다른 요소들을 쉽게 탐색할 수 있게 "추상화"한 장치임
    //  */
    // //////////////////////////////////////////////////////////////////////
    return 0;
}