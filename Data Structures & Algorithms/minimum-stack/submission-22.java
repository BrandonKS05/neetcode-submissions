class MinStack {

    class Node{
        int val;
        Node next;
        int minval;


        public Node(int val, int minval, Node next){
            this.val = val;
            this.next = next;
            this.minval = minval;
        }

    }

    Node head;
    int size;
    
    public MinStack() {
        head = null;
        size = 0;
    }
    
    public void push(int val) {
        int minval = (head == null) ? val : Math.min(head.minval, val);

        Node newNode = new Node(val, minval, head);

        head = newNode;
        size++;
    }
    
    public void pop() {
        if (head == null) return;
        head = head.next;   
        size--;
        
    }
    
    public int top() {
        if (head == null) return -1;
        return head.val;
        
    }
    
    public int getMin() {
        return head.minval;
    }
}
