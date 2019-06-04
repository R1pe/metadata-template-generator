#' @title malli_1 F0
#' @param a parameter a
#' @param c parameter c
#' @return x
#' @export
malli_1_F0 <- function(a,c)
{
    return(a+c)
}

#' @title malli_1 F1
#' @param b parameter b
#' @return c
#' @export
malli_1_F1 <- function(b)
{
    return(b*b*b+2)
}

#' @title malli_1 F2
#' @param a parameter a
#' @return c
#' @export
malli_1_F2 <- function(a)
{
    return(a*a*a)
}

