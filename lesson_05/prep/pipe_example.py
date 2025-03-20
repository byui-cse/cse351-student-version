import multiprocessing as mp

def child_process(conn):
    while True:
        message = conn.recv()  # Receive data from the parent
        if message is None:
            break
        print(f"Child: Received '{message}' from parent")
    print("Child Exiting")

    # very important to close the connect once finished using it
    conn.close()

def parent_process(conn):
    messages_to_send = ["one", 1, "two", 2, None]
    for message in messages_to_send:
        print(f"Parent: Sending '{message}' to child")
        conn.send(message)
    print("Parent Finished Sending")

    # very important to close the connect once finished using it
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = mp.Pipe()  # Create a bidirectional pipe

    parent = mp.Process(target=parent_process, args=(parent_conn,))
    child = mp.Process(target=child_process, args=(child_conn,))

    child.start()
    parent.start()

    parent.join()
    child.join()

    print("Both Parent and Child Exited")
