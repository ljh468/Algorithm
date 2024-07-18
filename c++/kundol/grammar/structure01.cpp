#include<bits/stdc++.h>
using namespace std;

int main(){
    //////////////////////////////////////////////////////////////////////
    /**
     * vector
     * 동적으로 요소를 할당할 수 있는 동적 배열
     * 만약 컴파일 시점에 사용해야할 요소들의 개수를 모른다면 vector를 써야함
     * 맨 앞이나 맨 뒤의 요소를 삭제하거나 삽입하는데 O(1), 다른 요소는 O(n)
     * vector<타입> 변수명;
     */
    //////////////////////////////////////////////////////////////////////
    vector<int> v;
    for(int i = 1; i <= 10; i++){
        v.push_back(i);
    }
    for(int a : v){
        cout << a << " ";
    }
    cout << "\n";
    // 1 2 3 4 5 6 7 8 9 10
    
    v.pop_back(); // 마지막 요소 제거
    for(int a : v){
        cout << a << " ";
    }
    cout << "\n";
    // 1 2 3 4 5 6 7 8 9

    v.erase(v.begin(), v.begin() + 3); // 인덱스 0부터 2까지 제거
    for(int a : v){
        cout << a << " ";
    }
    cout << "\n";

    // 4 5 6 7 8 9

    // vector<int>::iterator a = find(v.begin(), v.end(), 100);
    // if(a == v.end()){
    //     cout << "not found" << "\n";
    // }
    // // not found

    // fill(v.begin(), v.end(), 10);
    // for(int a : v){
    //     cout << a << " ";
    // }
    // cout << "\n";
    // // 10 10 10 10 10 10

    // v.clear();
    // cout << "아무것도 없을까?\n";
    // for(int a : v) {
    //     cout << a << "\n";
    // }
    // cout << "\n";

    //////////////////////////////////////////////////////////////////////
    /**
     * push_back()
     * vector의 뒤에서부터 요소를 더함
     * 같은 기능으로 emplace_back()도 있음
     * 
     * pop_back()
     * vector의 맨 뒤의 요소를 지움
     * 
     * erase()
     * iterator erase (const_iterator position);
     * iterator erase (const_iterator first, const_iterator last);
     * 한 요소만 지운다면 erase(위치)로 쓰이지만, 범위로 지우려면 erase[from, to)로 쓰임
     * 
     * find(from, to, value)
     * vector의 메서드가 아닌 STL 함수임
     * [from, to)에서 value를 찾아서 해당 시점의 이터레이터를 반환함
     * 찾지 못하면 .end() 시점을 반환함
     * 
     * clear()
     * vector의 모든 요소를 지움
     * 
     * fill(from, to, value)
     * vector내의 value로 값을 할당하고 싶다면 fill을 써서 채움
     * 이를 ~~ 한 값으로 초기화라고 함, [from, to) 구간에 value를 초기화, 전체 초기화시 사용
     */
    //////////////////////////////////////////////////////////////////////

    // //////////////////////////////////////////////////////////////////////
    // /**
    //  * 범위 기반 for loop
    //  * for(range_declearation : range_expression) loop_statemnet
    //  * for(<해당 컨테이너에 들어있는 타입> 임시 변수명 : 컨테이너)
    //  */
    // //////////////////////////////////////////////////////////////////////
    // vector<int> v = {1, 2, 3};
    // for(int a : v){
    //     cout << a << " ";
    // }
    // cout << "\n";

    // for(int i = 0; i < v.size(); i++){
    //     cout << v[i] << " ";
    // }
    // cout << "\n";

    // vector<pair<int, int>> v2 = {{1, 2}, {3, 4}};
    // for(pair<int, int> a : v2){
    //     cout << a.first << " ";
    // }

    // //////////////////////////////////////////////////////////////////////
    // /**
    //  * vector의 정적할당
    //  * vector라고 해서 무조건 크기가 0인 vector를 만들어서 동적할당으로 요소를 추가하는 것은 아님
    //  * 애초에 크기를 정해놓거나 어떠한 값으로 초기화해놓고 생성할 수 있음
    //  */
    // //////////////////////////////////////////////////////////////////////
    // vector<int> v = {10, 20, 30, 40 , 50};
    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL); cout.tie(NULL);
    // for(int i : v){
    //     cout << i << " ";
    // }

    // //////////////////////////////////////////////////////////////////////
    // /**
    //  * 2차원 배열
    //  * vector를 이용한 2차원 배열을 만드는 방법은 3가지임
    //  */
    // //////////////////////////////////////////////////////////////////////
    
    // // 1. vector안의 vector가 들어가 있는 2차원 배열 타입
    // vector<vector<int>> v;
    // for(int i = 0; i < 10; i++) {
    //     vector<int> temp(10, 0); // 내부 벡터를 10개의 0으로 초기화
    //     v.push_back(temp);
    // }
    // // 1-1. 값을 채우기
    // for(int i = 0; i < 10; i++) {
    //     for(int j = 0; j < 10; j++) {
    //         v[i][j] = i * 10 + j; // 예시: 순차적인 값으로 채우기
    //     }
    // }

    // // 1-2. 값 출력
    // cout << "2차원 배열 (방법 1):" << endl;
    // for(int i = 0; i < 10; i++) {
    //     cout << "{";
    //     for(int j = 0; j < 10; j++) {
    //         cout << v[i][j];
    //         if (j < 9) cout << ", "; // 마지막 요소가 아닌 경우에만 쉼표 추가
    //     }
    //     cout << "}";
    //     if (i < 9) cout << ", "; // 마지막 행이 아닌 경우에만 쉼표 추가
    // }
    // cout << "]" << endl;

    // cout << "######################################\n";
    
    // // 2. 10 * 10 크기의 2차원 배열을 바로 만들고 0으로 초기화
    // vector<vector<int>> v2(10, vector<int>(10, 0));
    // // 2-1. 값을 채우기
    // for(int i = 0; i < 10; i++) {
    //     for(int j = 0; j < 10; j++) {
    //         v2[i][j] = i * 10 + j; // 예시: 순차적인 값으로 채우기
    //     }
    // }

    // // 2-2. 값 출력
    // cout << "[";
    // for(int i = 0; i < 10; i++) {
    //     cout << "{";
    //     for(int j = 0; j < 10; j++) {
    //         cout << v2[i][j];
    //         if (j < 9) cout << ", "; // 마지막 요소가 아닌 경우에만 쉼표 추가
    //     }
    //     cout << "}";
    //     if (i < 9) cout << ", "; // 마지막 행이 아닌 경우에만 쉼표 추가
    // }
    // cout << "]" << endl;
    // cout << "######################################\n";

    // // 3. 10개 짜리 배열을 선언
    // vector<int> v3[10];
    // for(int i = 0; i < 10; i++) {
    //     v3[i] = vector<int>(10, 0); // 각 배열 요소에 10개의 0으로 초기화된 벡터를 할당
    // }

    // // 3-1. 값을 채우기
    // for(int i = 0; i < 10; i++) {
    //     for(int j = 0; j < 10; j++) {
    //         v3[i][j] = i * 10 + j; // 예시: 순차적인 값으로 채우기
    //     }
    // }

    // // 3-2. 값 출력
    // cout << "[";
    // for(int i = 0; i < 10; i++) {
    //     cout << "{";
    //     for(int j = 0; j < 10; j++) {
    //         cout << v3[i][j];
    //         if (j < 9) cout << ", "; // 마지막 요소가 아닌 경우에만 쉼표 추가
    //     }
    //     cout << "}";
    //     if (i < 9) cout << ", "; // 마지막 행이 아닌 경우에만 쉼표 추가
    // }
    // cout << "]" << endl;
    // cout << "######################################\n";

    // //////////////////////////////////////////////////////////////////////
    // /**
    //  * Array (정적배열)
    //  * 선언부터 크기를 설정함, 연속된 메모리 공간에 위치한 같은 타입의 요소들의 모음
    //  * c스타일, std스타일이 있음
    //  * - vector와 달리 메서드가 없음
    //  * - ex: int a[3];
    //  * - ex: int a2[] = {1, 2, 3, 4};
    //  * 앞의 코드처럼 하게 되면 자동적으로 rvalue의 크기로 할당되어 int a2[4]; 와 같은 의미를 가짐
    //  */
    // //////////////////////////////////////////////////////////////////////
    
    // // int a[3] = {1, 2, 3};
    // int a[3] = {1, 2, 3};
    // for(int i = 0; i < 3; i++){
    //     cout << a[i] << " ";
    // }
    // cout << "\n";

    // // int a2[] = {1, 2, 3, 4};
    // int a2[] = {1, 2, 3, 4};
    // for(int i : a2) {
    //     cout << i << " ";
    // }
    // cout << "\n";
    
    // // int a3[10];
    // int a3[10];
    // for(int i = 0; i < 10; i++){
    //     a3[i] = i;
    // }
    // for(int i : a3) {
    //     cout << i << " ";
    // }
    // cout << "\n";

    //////////////////////////////////////////////////////////////////////
    /**
     * 2차원배열과 탐색을 빠르게 하는 팁
     * - 2차원배열은 단순하게 차원을 늘려서 만들면 됨
     * - 첫번째 차원 >> 2번째 차원 순으로 탐색하는게 성능이 좋음
     * - C++에서 캐시를 첫번째 차원(여기서는 mxy가 되겠죠?) 를 기준으로 하기 때문에
     * - 캐시관련 효율성 때문에탐색을 하더라도 순서를 지켜가며 해주는게 좋음
     */
    //////////////////////////////////////////////////////////////////////
    const int mxy = 3;
    const int mxx = 4;

    int a[mxy][mxx];
    for(int i = 0; i < mxy; i++){
        for(int j = 0; j < mxx; j++){
            a[i][j] = (i + j);
        }
    }

    // good
    for(int i = 0; i < mxy; i++){
        for(int j = 0; j < mxx; j++){
            cout << a[i][j] << ' ';
        }
        cout << '\n';
    }

    // bad
    for(int i = 0; i < mxx; i++){
        for(int j = 0; j < mxy; j++){
            cout << a[j][i] << ' ';
        }
        cout << '\n';
    }
    return 0;
}