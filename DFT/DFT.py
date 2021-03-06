import numpy as np
import cmath as cm
import numpy as np

# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries


class DFT:

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        w,h=matrix.shape

        beta = [[0 for x in range(w)] for y in range(h)]

        for a in range(15):
            for b in range(15):
                asum = 0
                for i in range(15):
                    for j in range(15):
                        asum += matrix[i][j]*((np.cos(((2*np.pi)/15)*(a*i+b*j)))
                                             -(1j*np.sin(((2*np.pi)/15)*(a*i+b*j))))
                beta[a][b] = asum
        return beta

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        matrix: a 2d matrix (DFT) usually complex
        takes as input:
        returns a complex matrix representing the inverse fourier transform"""

        beta = [[0 for x in range(15)] for y in range(15)]

        for i in range(15):
            for j in range (15):
                asum = 0
                for u in range(15):
                    for v in range(15):
                        asum+=matrix[u][v]*((np.cos((2*np.pi/15)*(u*i+v*j)))
                                            +(1j*np.sin((2*np.pi/15)*(u*i+v*j))))
                beta[i][j] = asum
        return beta


    def discrete_cosine_tranform(self, matrix):
        """Computes the discrete cosine transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing discrete cosine transform"""
        w, h = matrix.shape

        beta = [[0 for x in range(w)] for y in range(h)]

        for a in range(h):
            for b in range(w):
                asum = 0
                for i in range(h):
                    for j in range(w):
                        asum += matrix[i][j]*(np.cos(((2 * np.pi)/w)*(a*i+b*j)))
                beta[a][b] = asum

        return beta


    def magnitude(self, matrix):
        """Computes the magnitude of the DFT
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the dft"""
        beta = [[0 for x in range(15)] for y in range(15)]
        for a in range(15):
            for b in range(15):
                beta[a][b] = np.absolute(matrix[a][b])
        return beta