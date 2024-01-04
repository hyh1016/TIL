# ReentrantLock

## Java에서 Critical Section(임계 영역)을 다루는 법

### synchronized

- 가장 기본적인 방법
- synchronized는 메서드 또는 스코프 단위로 락을 걸 수 있음
    - 메서드 방식
        
        ```java
        public synchronized void method() {
        	// critical section ...
        }
        ```
        
    - 스코프 방식
        
        ```java
        Object lock = new Object();
        
        public void method() {
        	// non-critical section ...
        	synchronized(lock) {
        		// critical section ...
        	}
        	// non-critical section ...
        }
        ```
        

### Synchronized의 단점

- 락이 걸린 리소스를 획득하고자 하는 스레드는 모두 `무한정 대기`하게 됨
    - 타임아웃 부여가 불가능
    - 리소스가 사용 불가능일 때 다른 작업을 하는 것이 불가능
- 임계 영역에 대한 세밀한 컨트롤이 어려움
    - 읽기 락, 쓰기 락과 같이 특정 조건에 따라 락을 거는 것이 불가능

### 대안 - ReentrantLock or ReentrantReadWriteLock

- `ReentrantLock`을 이용하면 synchronized보다 더 세부적인 락 컨트롤이 가능
- 또한, 더 향상된 `ReentrantReadWriteLock`을 통해 읽기 락과 쓰기 락을 각각 다루는 것도 가능

## ReentrantLock

### lock과 unlock

- synchronized는 락을 획득하는 lock 메서드만 존재한다면, ReentrantLock은 명시적으로 락을 해제하는 unlock 메서드도 존재
    
    ```java
    class MyConcurrentClass {
    	ReentrantLock reentrantLock = new ReentrantLock();
    
    	public void method() {
    		reentrantLock.lock();
    		try {
    			// critical section ...
    		} finally {
    			reentrantLock.unlock();
    		}
    	}
    }
    ```
    
    - **왜 finally 메서드를 사용하는가?**
        - unlock이 실행되지 않으면 해당 자원은 영영 락에 걸림
        - 이를 방지하기 위해 앞의 코드에서 예외가 던져져도 unlock 메서드는 반드시 실행되어야 하기 때문에, finally 내에서 호출

### tryLock

- synchronized의 단점 중 한 가지는 lock을 획득할 수 없는 스레드들이 무한정 대기에 빠진다는 것
- ReentrantLock은 tryLock이라는 메서드를 제공하며, 두 가지 방식으로  사용 가능
    1. 즉시 획득 시도 후 실패 시 넘어감
        
        ```java
        class MyConcurrentClass {
        	ReentrantLock reentrantLock = new ReentrantLock();
        
        	public void method() {
        		if (reentrantLock.tryLock()) {
        			try {
        				// critical section ...
        			} finally {
        				reentrantLock.unlock();
        			}
        		}
        	}
        }
        ```
        
        - 락을 획득할 수 있을 때에만 method가 실행되고 아닐 때에는 else 문 실행
    2. 특정 시간 동안 획득 시도 후 실패 시 넘어감
        
        ```java
        class MyConcurrentClass {
        	ReentrantLock reentrantLock = new ReentrantLock();
        
        	public void method() {
        		if (reentrantLock.tryLock(3, TimeUnit.SECONDS)) {
        			try {
        				// critical section ...
        			} finally {
        				reentrantLock.unlock();
        			}
        		}
        	}
        }
        ```
        
        - 3초 동안 락 획득을 대기하고 획득 시 method  실행, 아니면 else 문 실행
- **왜 중요한가?**
    - 무한정 대기하는 것은 위험. 특히 사용자와 interaction이 존재하는 애플리케이션이라면 더더욱 위험
    - 이를 위해 실제로는 동기화된 리소스에 접근하기 위해 lock 획득을 기다리고 있더라도, 사용자에게는 실시간으로 반응을 보여줄 수 있어야 함
        - 이걸 else 문에서 하면 된다는 것

## ReentrantReadWriteLock

### Lock에 의한 성능 저하

- 위의 ReentrantLock의 경우 synchronized보다 유연하다는 장점은 있으나, 임계 영역이 많아질 수록 성능이 저하되는 정도는 synchronized와 동일함
- 읽기 락과 쓰기 락을 통해 특정 조건에서는 스레드가 리소스에 동시에 접근할 수 있도록 허용하여 성능 저하를 일부 회복 가능

### 읽기 락과 쓰기 락

- **읽기 락**
    - 읽기 락은 여러 스레드가 동시에 획득이 가능
    - 모든 읽기 락이 해제될 때까지 쓰기 락은 획득 불가능
- **쓰기 락**
    - 한 번에 하나의 스레드만 획득 가능
    - 쓰기 락이 해제될 때까지 읽기 락 획득 불가능
- **예시**
    
    ```java
    class MyConcurrentClass {
        ReentrantReadWriteLock readWriteLock = new ReentrantReadWriteLock();
        Lock readLock = readWriteLock.readLock();
        Lock writeLock = readWriteLock.writeLock();
    
        public void read() {
            if (readLock.tryLock()) {
                try {
                    System.out.println("critical section");
                } finally {
                    readLock.unlock();
                }
            } else {
                System.out.println("fail to get read lock");
            }
        }
    
        public void write() {
            if (writeLock.tryLock()) {
                try {
                    System.out.println("critical section");
                } finally {
                    writeLock.unlock();
                }
            } else {
                System.out.println("fail to get read lock");
            }
        }
    }
    ```
    
    - read 메서드는 readLock을 이용하므로 한 번에 여러 스레드에서 수행 가능하지만 write 메서드를 호출 중인 스레드가 하나라도 있다면 실행 불가능
    - write 메서드는 read 또는 write 메서드를 수행 중인 스레드가 하나라도 있다면 실행 불가능
