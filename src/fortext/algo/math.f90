subroutine factorial(n, result)
    integer, intent(in) :: n
    integer, intent(out) :: result
    integer :: i

    result = 1
    do i = 1, n
        result = result * i
    end do
end subroutine factorial