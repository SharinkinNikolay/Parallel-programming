﻿#include <cstdio>
#include "mpi.h"

int main(int* argc, char** argv)
{
    MPI_Init(argc, &argv);

    printf("Hello, world!");

    MPI_Finalize();

    return 0;
}
