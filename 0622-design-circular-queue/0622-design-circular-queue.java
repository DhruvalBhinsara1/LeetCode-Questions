class MyCircularQueue {

    int[] q;
    int front;
    int rear;
    int capacity;
    int count;

    public MyCircularQueue(int k) {
        q = new int[k];
        front =0;
        rear =-1;    
        capacity =k;
        count =0;
        }
    
    public boolean enQueue(int value) {
        if (isFull()){
            return false;
        }
        rear = (rear+1)% capacity;
        q[rear]=value;
        count++;
        return true;
    }
    
    public boolean deQueue() {
        if(isEmpty()){
            return false;
        }

        front = (front+1)%capacity;
        count--;
        return true;
    }
    
    public int Front() {
        if(isEmpty()) return -1;

        return q[front];
    }
    
    public int Rear() {
        if(isEmpty()) return -1;

        return q[rear];
    }
    
    public boolean isEmpty() {
        if(count==0){
            return true;
        }
        else{
            return false;
        }
    }
    
    public boolean isFull() {
        if(count == capacity){
            return true;
        }

        else{
            return false;
        }
    }
}