#include "mpi.h"
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

std::vector<int> parseVector(const std::string& str) {
    std::vector<int> vec;
    std::istringstream iss(str);
    int val;
    while (iss >> val) {
        vec.push_back(val);
        if (iss.peek() == ',') {
            iss.ignore();
        }
    }
    return vec;
}

int main(int argc, char* argv[]) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (argc < 3) {
        if (rank == 0) {
            std::cout << "Error: not enough comand line arguments." << std::endl;
        }
        MPI_Finalize();
        return 1;
    }

    std::vector<int> vec1 = parseVector(argv[1]);
    std::vector<int> vec2 = parseVector(argv[2]);

    if (vec1.size() != vec2.size()) {
        if (rank == 0) {
            std::cout << "Error: Vector dimensions do not match." << std::endl;
        }
        MPI_Finalize();
        return 1;
    }

    int n = vec1.size();
    int chunk = n / size;
    int remainder = n % size;

    std::vector<int> local_result(chunk + (rank < remainder));
    int start = rank * chunk + std::min(rank, remainder);
    int end = start + local_result.size();

    for (int i = start; i < end; i++) {
        local_result[i - start] = vec1[i] + vec2[i];
    }

    std::vector<int> result(n);
    int* recvcounts = new int[size];
    int* displs = new int[size];

    for (int i = 0; i < size; i++) {
        recvcounts[i] = chunk + (i < remainder);
        displs[i] = i * chunk + std::min(i, remainder);
    }

    MPI_Gatherv(&local_result[0], local_result.size(), MPI_INT, &result[0], recvcounts, displs, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        std::cout << "Result: ";
        for (int val : result) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }

    delete[] recvcounts;
    delete[] displs;
    MPI_Finalize();
    return 0;
}
