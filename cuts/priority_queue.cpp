// Priority queue implementation in C++ using heapq
// Avaliable methods are: 
// void Enqueue(string obj, int priority)
// std::string Dequeue()
// The bigger the priority number, the higher the priority
// On the same priority will be used FIFO


class PriorityQueue {
private:
    std::priority_queue<std::tuple<int, int, std::string>> queue;
    int counter;
public:
    PriorityQueue() : counter(0) {}

    void Enqueue(std::string obj, int priority) {
        queue.push(std::make_tuple(priority, counter++, obj));
    }

    std::string Dequeue() {
        if (queue.empty()) {
            throw std::runtime_error("Dequeue from an empty priority queue");
        }
        std::string result = std::get<2>(queue.top());
        queue.pop();
        return result;
    }
};


class PriorityQueue2 {
private:
    std::vector<std::tuple<int, int, std::string>> queue;
    int counter;

    int FindHighestPriorityIndex() {
        if (queue.empty()) {
            throw std::runtime_error("Dequeue from an empty priority queue");
        }

        int highestPriorityIndex = 0;
        for (int i = 1; i < queue.size(); ++i) {
            if (std::get<0>(queue[i]) > std::get<0>(queue[highestPriorityIndex]) || 
                (std::get<0>(queue[i]) == std::get<0>(queue[highestPriorityIndex]) &&
                std::get<1>(queue[i]) < std::get<1>(queue[highestPriorityIndex]))) {
                highestPriorityIndex = i;
            }
        }

        return highestPriorityIndex;
    }
public:
    PriorityQueue2() : counter(0) {}

    void Enqueue(std::string obj, int priority) {
        queue.push_back(std::make_tuple(priority, counter++, obj));
    }

    std::string Dequeue() {
        int highestPriorityIndex = FindHighestPriorityIndex();
        std::string obj = std::get<2>(queue[highestPriorityIndex]);
        queue.erase(queue.begin() + highestPriorityIndex);
        return obj;
    }
}
