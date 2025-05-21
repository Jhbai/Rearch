#include <stdlib.h>
#include <math.h>
#include "_pelt.h"

double squared_distance(const double *seq1, const double *seq2, int len) {
    double sum = 0.0;
    for (int i = 0; i < len; ++i) {
        double diff = seq1[i] - seq2[i];
        sum += diff * diff;
    }
    return sum;
}

void pelt_segment(
    const double *serie, int n,
    const double *query, int q,
    double *out_best_dist,
    int *out_best_start,
    int *out_best_end
) {
    if (q == 0 || n < q) {
        *out_best_dist = INFINITY;
        *out_best_start = -1;
        *out_best_end = -1;
        return;
    }

    double overall_min = INFINITY;
    int best_i = -1, best_j = -1;

    for (int offset = 0; offset < q; ++offset) {
        double min_offset = INFINITY;
        int start_off = -1, end_off = -1;

        for (int k = q; k <= n; ++k) {
            int i = k - q;
            if (i % q != offset) continue;

            double d = squared_distance(query, serie + i, q);
            if (d < min_offset) {
                min_offset = d;
                start_off = i;
                end_off = k - 1;
            }
        }

        if (min_offset < overall_min) {
            overall_min = min_offset;
            best_i = start_off;
            best_j = end_off;
        }
    }

    *out_best_dist = overall_min;
    *out_best_start = best_i;
    *out_best_end = best_j;
}
