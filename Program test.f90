 program test
   implicit none
   
   integer :: i
   real :: npp_pls(5), mass_seed(5)
   real :: a, b
   
   call random_seed() ! inicializa a semente do gerador de números aleatórios
   a = 0.5 ! limite inferior
   b = 5.0 ! limite superior
   
   do i = 1, 5
      call random_number(npp_pls(i))
      npp_pls(i) = a + (b-a)*npp_pls(i) ! escala para o intervalo desejado
   end do
   
   ! imprime os números gerados
   write(*,*) "Números gerados:"
   do i = 1, 5
    write(*,*) npp_pls(i)
   end do

   do i = 1, 5
      call random_number(mass_seed(i))
      mass_seed(i) = a + (b-a)*mass_seed(i) ! escala para o intervalo desejado
   end do
   
   ! imprime os números gerados
   print*, "Números gerados:"
   do i = 1, 5
   print*, mass_seed(i)
   end do


end program test