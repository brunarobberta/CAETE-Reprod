program lista_fortran

implicit none

real :: lista1(5), lista2(5), lista1_nova(5), lista_final(5)
real :: adicao(10) = 0.0 ! vetor com adição a ser aplicada em cada tempo
integer :: i, j
logical :: is_time1

! repetir o código 10 vezes
do j = 1, 10

  ! determinar o tempo atual
  is_time1 = (j == 1)

  ! gerando a lista1 com valores de 0.5 a 5
  do i = 1, 5
    lista1(i) = 0.5*(i+1)
  end do

  ! gerando a lista2 com valores de 1 a 5
  do i = 1, 5
    lista2(i) = i
  end do

  ! tirando 90% de cada número da lista1
  lista1_nova = lista1*0.1

  ! dividindo os números da lista1_nova com os números da lista2,
  ! com condição de que os números da lista1_nova sejam maiores que 0
  do i = 1, 5
    if (lista1_nova(i) > 0) then
      lista_final(i) = lista1_nova(i) / lista2(i)
    else
      lista_final(i) = 0.0
    end if
  end do

  ! calculando os números da lista final deixando apenas 60% de cada item
  lista_final = lista_final*0.6

  ! dividindo por 60% se é tempo 1, ou usando o valor de 60% mais a adição do tempo 1
  if (is_time1) then
    lista_final = lista_final / 0.6
  else
    lista_final = (lista_final / 0.6) + adicao(j)
  end if

  ! garantindo que nenhum valor seja abaixo de 0
  lista_final = max(lista_final, 0.0)

  ! arredondando todos os valores para duas casas decimais
  lista1 = nint(lista1*100)/100.0
  lista2 = nint(lista2*100)/100.0
  lista1_nova = nint(lista1_nova*100)/100.0
  lista_final = nint(lista_final*100)/100.0

  ! exibindo o resultado final
  write(*,*) 'Iteração ', j
  write(*,*) 'Lista1: ', lista1, ' Lista2: ', lista2
  write(*,*) 'Lista1 nova (após tirar 90%): ', lista1_nova
  write(*,*) 'Lista final (após dividir pela lista2 e aplicar regra de tempo): ', lista_final

end do

end program lista_fortran
