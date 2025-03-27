# Lesson 9: Classic Concurrency Problems

**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
9.1 | [Patterns](#Patterns)
9.2 | [The Producer-Consumer Problem](#The-Producer-Consumer-Problem)
9.3 | [The Readers-Writers Problem](#The-Readers-Writers-Problem)
9.4 | [The Dining Philosophers Problem](#The-Dining-Philosophers-Problem)
9.5 | [Monte Carlo Simulations](#Monte-Carlo-Simulations)
9.6 | [Other Classic Problems](#Other-Classic-Problems)

:key: = Vital concepts that we will continue to build on in coming lessons / key learning outcomes for this course.


# Common Programming Patterns

## Boss-Worker Pattern

The Boss-Worker pattern involves a "boss" thread that distributes tasks to multiple "worker" threads. The boss thread is responsible for task creation and distribution, while worker threads perform the actual work.  This pattern is useful for parallelizing tasks that can be divided into independent subtasks.

#### Boss

- Creates and manages worker threads.
- Divides the workload into smaller tasks.
- Distributes tasks to available workers.
- May collect and aggregate results from workers.


#### Workers

- Receive tasks from the boss.
- Execute the tasks independently.
- May return results to the boss.


```mermaid
graph LR
    B[Boss] -- "Adds Tasks" --> Q{Queue};
    Q -- "Gets Task" --> W1[Worker 1];
    Q -- "Gets Task" --> W2[Worker 2];
    Q -- "Gets Task" --> W3[Worker 3];
    Q -- "Gets Task" --> WN[... Worker N ...];

    style B fill:#ff0000,stroke:#333,stroke-width:2px
    style W1 fill:#00ff,stroke:#333,stroke-width:1px
    style W2 fill:#00ff,stroke:#333,stroke-width:1px
    style W3 fill:#00ff,stroke:#333,stroke-width:1px
    style WN fill:#00ff,stroke:#aaa,stroke-width:1px,stroke-dasharray: 5 5
```

### Code Example

```python
```

## Producer-Consumer Pattern

The Producer-Consumer pattern involves one or more "producer" threads that generate data and one or more "consumer" threads that process that data.
A shared buffer is used to hold the data between producers and consumers.
This pattern is useful for decoupling data generation from data processing.

#### Producers
- Generate data.
- Place data into the shared buffer.
- Signal consumers when data is available.


#### Consumers
- Retrieve data from the shared buffer.
- Process the data.
- Signal producers when buffer space is available.

```mermaid
graph LR
    subgraph Producers
        direction TB  
        P1(Producer 1)
        P2(Producer 2)
        PN(...)        
    end

    subgraph Consumers
        direction TB  
        C1(Consumer 1)
        C2(Consumer 2)
        CN(...)        
    end

    subgraph SharedResource
       direction TB
        B{Shared Buffer / Queue}; 
    end


    P1 -- "Adds Item (Waits if Full)" --> B;
    P2 -- "Adds Item (Waits if Full)" --> B;
    PN -- "Adds Item (Waits if Full)" --> B;

    B -- "Removes Item (Waits if Empty)" --> C1;
    B -- "Removes Item (Waits if Empty)" --> C2;
    B -- "Removes Item (Waits if Empty)" --> CN;

%% Styling
style Producers fill:#ff0000,stroke:#ddd
style Consumers fill:#0000ff,stroke:#ddd
style SharedResource fill:#00ff00,stroke:#ddd,color:#000000

style P1 fill:#00,stroke:#333,stroke-width:2px
style P2 fill:#00,stroke:#333,stroke-width:2px
style PN fill:#00,stroke:#aaa,stroke-width:1px,stroke-dasharray: 5 5

style C1 fill:#00,stroke:#333,stroke-width:2px
style C2 fill:#00,stroke:#333,stroke-width:2px
style CN fill:#00,stroke:#aaa,stroke-width:1px,stroke-dasharray: 5 5

style B fill:#00,stroke:#333,stroke-width:2px
```

### Code Example

```python
```

## Bounded Buffer

A Bounded Buffer is a variation of the Producer-Consumer pattern where the shared buffer has a fixed size.  Producers wait if the buffer is full, and consumers wait if the buffer is empty.  This pattern is used to control the rate of data production and consumption.

#### Details
- Implements a fixed-size buffer.
- Uses synchronization mechanisms (e.g., 2 semaphores) to manage buffer access.  Each semaphore handles the "ends" of the buffer.  One for index == 0 and one for index == (N-1)
- Producers block when the buffer is full.
- Consumers block when the buffer is empty.

```mermaid
graph LR
    subgraph Producers
        direction TB
        P1(Producer 1)
        P2(...)
    end

    subgraph Consumers
        direction TB
        C1(Consumer 1)
        C2(...)
    end

    subgraph SharedResource
       direction TB
        BB{Bounded Buffer<br>count == N}
    end

    P1 -- "put(item)<br>[Waits if Full (count==N)]" --> BB;
    P2 -- "put(item)<br>[Waits if Full (count==N)]" --> BB;

    BB -- "get()<br>[Waits if Empty (count==0)]" --> C1;
    BB -- "get()<br>[Waits if Empty (count==0)]" --> C2;

%% Styling (similar to previous)
style Producers fill:#ff0000,stroke:#ddd
style Consumers fill:#0000ff,stroke:#ddd
style SharedResource fill:#00ff00,stroke:#ddd,color:#000000

style P1 fill:#ccf,stroke:#333,stroke-width:2px,color:#000
style P2 fill:#eee,stroke:#aaa,stroke-width:1px,stroke-dasharray: 5 5,color:#000

style C1 fill:#ffc,stroke:#333,stroke-width:2px,color:#000
style C2 fill:#eee,stroke:#aaa,stroke-width:1px,stroke-dasharray: 5 5,color:#000

style BB fill:#f9f,stroke:#333,stroke-width:2px,color:#000
```

### Code Example

```python
```

## Client-Server Pattern

The Client-Server pattern involves a "server" that provides services to multiple "clients."  Clients send requests to the server, and the server processes the requests and sends responses back to the clients.  This pattern is fundamental to network applications.

#### Server
- Listens for client connections.
- Accepts client requests.
- Processes requests concurrently (using threads or tasks).
- Sends responses to clients.


#### Clients
- Connect to the server.
- Send requests to the server.
- Receive responses from the server.

TODO - Add image


```mermaid
graph LR
    subgraph Clients
        direction TB
        C1(Client 1)
        C2(Client 2)
        CN(...)
    end

    subgraph Network_Infrastructure
       N[Network]
    end

    subgraph ServerSide
       S((Server))
    end

    Clients -- Request --> N;
    N -- Request --> ServerSide;
    ServerSide -- Response --> N;
    N -- Response --> Clients;

%% Styling
style Clients fill:#f8f8f8,stroke:#ddd,color:#000
style Network_Infrastructure fill:#f8f8f8,stroke:#ddd,color:#000
style ServerSide fill:#f8f8f8,stroke:#ddd,color:#000

style C1 fill:#ccf,stroke:#333,stroke-width:1px,color:#000
style C2 fill:#ccf,stroke:#333,stroke-width:1px,color:#000
style CN fill:#eee,stroke:#aaa,stroke-width:1px,stroke-dasharray: 5 5,color:#000
style N fill:#f5f5f5,stroke:#999,stroke-width:1px,color:#000
style S fill:#ffc,stroke:#333,stroke-width:2px,color:#000
```

### Code Example

```python
```

## Reader-Writer Problem

The Reader-Writer problem involves managing concurrent access to a shared resource, where multiple readers can access the resource simultaneously, but writers require exclusive access.  The challenge is to allow concurrent reads while preventing data corruption when a writer modifies the resource.

#### Readers

Can access the resource concurrently as long as no writer is active.

#### Writers

Need exclusive access to modify the resource.

#### Potential Issues
- Starvation: Writers may be starved if there is a continuous stream of readers.
- Deadlocks: If readers and writers acquire locks in different orders, deadlocks can occur.

TODO - Add image

```mermaid
stateDiagram-v2
    %% Define the possible states of the shared resource
    state "Shared Resource State" as Resource {
        Idle : No active readers or writers
        Reading : One or more readers are active
        Writing : Exactly one writer is active
    }

    [*] --> Idle : Initialization

    %% Transitions based on arriving actors
    Idle --> Reading : Reader Arrives\n[No Writer Active]
    Reading --> Reading : Reader Arrives\n[No Writer Active]

    Idle --> Writing : Writer Arrives\n[No Reader or Writer Active]

    %% Transitions based on departing actors
    Reading --> Idle : Last Reader Leaves
    Writing --> Idle : Writer Leaves


    %% Notes explaining concurrency rules and blocking
    note right of Reading
        - Multiple readers allowed concurrently.
        - Arriving readers are granted access.
        - Arriving writers **must wait**.
    end note

    note left of Writing
        - Only one writer allowed.
        - Arriving readers **must wait**.
        - Arriving writers **must wait**.
    end note

    %% --- Implicit Blocking ---
    %% The diagram primarily shows allowed transitions.
    %% Requests that cannot proceed immediately cause the requesting
    %% process/thread to block (wait) until the state changes.
    %% For example:
    %% - A Writer arriving in the Reading state blocks.
    %% - A Reader arriving in the Writing state blocks.
    %% - A Writer arriving in the Writing state blocks.
```

```mermaid
stateDiagram-v2
    [*] --> Idle : Initialization

    state "Resource State" as RState {
        Idle : No one accessing
        Reading : 1+ Readers accessing
        Writing : 1 Writer accessing
    }

    Idle --> Reading : Reader Arrives\n[No Writer Present]
    Reading --> Reading : Another Reader Arrives\n[No Writer Present]
    Reading --> Idle : Last Reader Leaves

    Idle --> Writing : Writer Arrives\n[No Reader/Writer Present]
    Writing --> Idle : Writer Leaves

    note right of Reading
        Multiple readers OK.
        Writers must wait.
    end note

    note right of Writing
        Only one writer allowed.
        Readers must wait.
        Other Writers must wait.
    end note

    %% Implicit: Requests arriving when not allowed cause waiting.
    %% e.g., Writer arriving during Reading state waits.
    %% e.g., Reader arriving during Writing state waits.
```

```mermaid
stateDiagram-v2
    direction LR
    [*] --> Idle : Start

    Idle --> Reading : Reader Arrives [No Writer]
    Reading --> Reading : Reader Arrives [No Writer]
    Reading --> Idle : Last Reader Leaves

    Idle --> Writing : Writer Arrives [No Reader or Writer]
    Writing --> Idle : Writer Leaves

    %% Dashed lines for requests that cause waiting (conceptual)
    Reading --> Writing : Writer Arrives [Readers Active] -- Wait --> Writing
    Writing --> Reading : Reader Arrives [Writer Active] -- Wait --> Reading
    Writing --> Writing : Writer Arrives [Writer Active] -- Wait --> Writing
```

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Reading : Reader Arrives\n(No Writer)
    Idle --> Writing : Writer Arrives\n(No Reader/Writer)

    state Reading {
         [*] --> Active : Reader Enters
         Active --> Active : Another Reader Arrives\n(No Writer)
         Active --> [*] : Last Reader Leaves
    }

    Reading --> Idle : Last Reader Leaves

    state Writing {
         [*] --> Active : Writer Enters
         Active --> [*] : Writer Leaves
    }

    Writing --> Idle : Writer Leaves

    %% Notes indicating blocking conditions (Conceptual)
    %% Note right of Reading : Writers must wait
    %% Note right of Writing : Readers must wait
    %% Note right of Writing : Other Writers must wait
```

```mermaid
graph TD
    subgraph Actors
        R[Readers Multiple Concurrent]
        W[Writer Exclusive Access]
    end

    subgraph Synchronization
        AC{Access Control\nAllows Multiple Readers OR One Writer}
    end

    subgraph Data
        SR[Shared Resource]
    end

    R -- "Request Read" --> AC;
    W -- "Request Write" --> AC;
    AC -- "Grant Read (if no writer)" --> SR;
    AC -- "Grant Write (if no reader/writer)" --> SR;
    SR -- "Read Data" --> R;
    SR -- "Write Data" --> W;

    %% Styling
    style R fill:#ccf,stroke:#333,color:#000
    style W fill:#ffc,stroke:#333,color:#000
    style AC fill:#f9f,stroke:#333,color:#000
    style SR fill:#cfc,stroke:#333,color:#000
```

```mermaid
graph TD
    subgraph Actors
        R((Readers\nMultiple OK))
        W((Writer\nExclusive))
    end

    subgraph Synchronization
         AC{Access Control Logic}
    end

    subgraph Data
         SR[Shared Resource]
    end

    R -- "Request Read" --> AC;
    W -- "Request Write" --> AC;
    AC -- "Grant Access\n(According to Rules)" --> SR;


    %% Styling
    style Actors fill:#f8f8f8,stroke:#ddd
    style Synchronization fill:#f8f8f8,stroke:#ddd
    style Data fill:#f8f8f8,stroke:#ddd

    style R fill:#ccf,stroke:#333,color:#000
    style W fill:#ffc,stroke:#333,color:#000
    style AC fill:#f9f,stroke:#333,color:#000
    style SR fill:#cfc,stroke:#333,color:#000
```

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Reading : Reader Arrives [Writer Idle]
    Reading --> Reading : Reader Arrives [Writer Idle]
    Reading --> Idle : Last Reader Leaves

    Idle --> Writing : Writer Arrives [No one Active]
    Writing --> Idle : Writer Leaves

    %% Note: Waiting/blocking is implied when conditions aren't met.
```

```mermaid
graph TD
    subgraph Actors
        R((Readers\nMultiple OK))
        W((Writer\nExclusive Access))
    end

    subgraph Synchronization
         AC{Access Control Logic\n Locks/Semaphores/etc. synchronization mechanism}
    end

    subgraph Data
         SR[Shared Resource]
    end

    R -- "Request Read" --> AC;
    W -- "Request Write" --> AC;
    AC -- "Grant Access\n(If Rules Allow)" --> SR;


    %% Styling
    style Actors fill:#f8f8f8,stroke:#ddd
    style Synchronization fill:#f8f8f8,stroke:#ddd
    style Data fill:#f8f8f8,stroke:#ddd

    style R fill:#ccf,stroke:#333,color:#000
    style W fill:#ffc,stroke:#333,color:#000
    style AC fill:#f9f,stroke:#333,color:#000
    style SR fill:#cfc,stroke:#333,color:#000
```

```mermaid
```


### Code Example

```python
```

## Dining Philosophers Problem

The Dining Philosophers problem illustrates a classic synchronization issue where multiple philosophers sit around a table with a single chopstick between each pair.  Each philosopher needs two chopsticks to eat, but they can only pick up one chopstick at a time.  The challenge is to prevent deadlocks where each philosopher holds one chopstick and waits indefinitely for the other.


#### Philosophers

Need two chopsticks (resources) to eat.

#### Chopsticks

Shared resources that can only be used by one philosopher at a time.

#### Potential Issue

- Deadlock if all philosophers pick up their left chopstick simultaneously.

TODO - Add image

### Code Example

```python
```

## Sleeping Barber Problem

The Sleeping Barber problem models a barber shop with a single barber and a limited number of waiting chairs.  The barber sleeps when there are no customers, and customers leave if there are no available chairs.  The challenge is to ensure that the barber and customers coordinate properly to avoid race conditions and deadlocks.


#### Barber

Sleeps when there are no customers, wakes up when a customer arrives.
#### Customers

Enter the shop if there is an available chair, otherwise leave.
#### Waiting Chairs

Limited number of chairs for waiting customers.

#### Potential Issues
- Race Condition: Multiple customers might try to wake up the barber simultaneously.
- Deadlock: The barber might be waiting for a customer while a customer is waiting for the barber.

TODO - Add image

### Code Example

```python
```

## Elevator Simulation

Simulate the behavior of an elevator system with multiple elevators, floors, and passengers.  The simulation should handle passenger requests, elevator movement, and floor selection.  This problem demonstrates concurrent process interactions and resource management.

#### Elevators

Move between floors, have capacity limits, and door open/close mechanisms.

#### Floors

Passengers request elevators from floors, and elevators arrive at floors.

#### Passengers

Generate requests with source and destination floors.

#### Challenges
- Coordinating elevator movement to minimize waiting time and travel distance.
- Handling concurrent passenger requests efficiently.
- Avoiding collisions and deadlocks.

TODO - Add image

### Code Example

```python
```


## Cigarette Smokers Problem

The Cigarette Smokers problem is a classic concurrency problem that illustrates synchronization challenges.  Three smokers have different resources (tobacco, paper, matches), and an agent provides two of the three resources at a time.  Each smoker needs all three resources to make a cigarette, but they can only acquire the resources provided by the agent.  The challenge is to synchronize the smokers and the agent to avoid deadlocks and ensure progress.


#### Smokers

Each smoker has one of the three resources and needs the other two.

#### Agent

Randomly provides two of the three resources.

#### Challenges

- Ensuring that only one smoker can acquire the necessary resources at a time.
- Preventing deadlocks where smokers wait indefinitely for the missing resource.

TODO - Add image

### Code Example

```python

```

## Monte Carlo Simulations

Monte Carlo simulations use random sampling to estimate numerical results.  These simulations are often used in finance, physics, and engineering.  Parallelizing Monte Carlo simulations can significantly improve performance.

#### Random Number Generation

Generate a large number of random samples.

#### Computation

Perform calculations on each sample.

#### Aggregation

Aggregate the results from all samples.

#### Challenges
- Ensuring that random number generation is thread-safe.
- Efficiently distributing the workload across multiple threads or tasks.

TODO - Add image

### Code Example

```python
```
