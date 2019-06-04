#' @title malli_1_ParRaj F0
#' @param a parameter a
#' @param c parameter c
#' @check a {2,3}
#' @check c (0,)
#' @return x
#' @export
malli_1_ParRaj_F0 <- function(a,c)
{
  return(a+c)
}

#' @title malli_1_ParRaj F1
#' @param a parameter a
#' @param c parameter c
#' @check a {1}
#' @check c (...)             TODO: != 0?
#' @return x
#' @export
malli_1_ParRaj_F1 <- function(a,c)
{
  return(10 + a + c)
}

#' @title malli_1_ParRaj F2
#' @param a parameter a
#' @param c parameter c
#' @check a (,0)
#' @check c (,0)
#' @return x
#' @export
malli_1_ParRaj_F2 <- function(a,c)
{
  return(20 + a + c)
}

#' @title malli_1_ParRaj F3
#' @param a parameter a
#' @param c parameter c
#' @check a (,0)
#' @check c (0,)
#' @return x
#' @export
malli_1_ParRaj_F3 <- function(a,c)
{
  return(30 + a + c)
}

#' @title malli_1_ParRaj F4
#' @param a parameter a
#' @param b parameter b
#' @check a {2,3}
#' @check b (0,4)
#' @return c
#' @export
malli_1_ParRaj_F4 <- function(a,b)
{
  return(40 + 0*a + 0*c)
}

#' @title malli_1_ParRaj F5
#' @param a parameter a
#' @param b parameter b
#' @check a {1,-2}
#' @check b (,0)
#' @return c
#' @export
malli_1_ParRaj_F5 <- function(a,b)
{
  return(50 + 0*a + 0*c)
}
