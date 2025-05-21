# cython: boundscheck=False, wraparound=False
import numpy as np
cimport numpy as np

cdef extern from "_pelt.h":
    double squared_distance(const double *seq1, const double *seq2, int len)
    void pelt_segment(
        const double *serie, int n,
        const double *query, int q,
        double *out_best_dist,
        int *out_best_start,
        int *out_best_end
    )

def find_best_fixed_length_segment(np.ndarray[np.double_t, ndim=1] query,
                                   np.ndarray[np.double_t, ndim=1] serie):
    """
    Cython 包裝的 PELT-like 固定長度搜尋。
    回傳 (最小距離, 起始索引, 結束索引)。
    """
    cdef int n = serie.shape[0]
    cdef int q = query.shape[0]
    cdef double best_dist
    cdef int best_start, best_end

    pelt_segment(<const double*>serie.data, n,
                 <const double*>query.data, q,
                 &best_dist,
                 &best_start,
                 &best_end)

    return best_dist, best_start, best_end
