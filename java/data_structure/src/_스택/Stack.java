package _스택;

import _연결리스트.Node;

public class Stack {

  private int size;

  private Node head;

  public Stack() {
    this.size = 0;
    this.head = null;
  }

  public void push(int data) {
    Node newNode = new Node(data);
    if (this.head != null) {
      newNode.setNext(head);
    }
    this.head = newNode;
    size++;
  }

  public Node pop() {
    if (head != null) {
      Node popNode = this.head;
      size--;
      this.head = this.head.getNext();
      return popNode;
    }
    return null;
  }

  public Node peek() {
    return this.head;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public static void main(String[] args) {
    Stack stack = new Stack();
    System.out.println("===== 1, 2, 3, 4를 순서대로 스택에 push =====");
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);

    System.out.println("===== 스택에서 4번 pop() =====");
    System.out.println("stack.pop().getData() = " + stack.pop().getData());
    System.out.println("stack.pop().getData() = " + stack.pop().getData());
    System.out.println("stack.pop().getData() = " + stack.pop().getData());
    System.out.println("stack.pop().getData() = " + stack.pop().getData());

    System.out.println("===== 다시 1부터 4까지 스택에 push =====");
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);

    System.out.println("stack.peek() = " + stack.peek().getData());
    System.out.println("stack.pop() = " + stack.pop().getData());
    System.out.println("stack.peek() = " + stack.peek().getData());
    System.out.println("stack.isEmpty() = " + stack.isEmpty());
    System.out.println("stack.pop() = " + stack.pop().getData());
    System.out.println("stack.pop() = " + stack.pop().getData());
    System.out.println("stack.pop() = " + stack.pop().getData());
    System.out.println("stack.isEmpty() = " + stack.isEmpty());
    System.out.println("stack.pop() = " + stack.pop());
  }
}
