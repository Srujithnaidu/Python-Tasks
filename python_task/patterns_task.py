# # 1 
# # 2 2 
# # 3 3 3 
# # 4 4 4 4 
# # 5 5 5 5 5 
# for i in range(1,6,1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# # ======================================
# # 5
# # 4 4
# # 3 3 3
# # 2 2 2 2
# # 1 1 1 1 1 
# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(i,end=" ")
#     print()

# # ======================================
# #         1 
# #       2 2 
# #     3 3 3 
# #   4 4 4 4 
# # 5 5 5 5 5 
# for i in range(1,6,1):
#     for s in range(5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1,1):
#         print(i,end=" ")
#     print()

# # =========================================
# # 5 5 5 5 5 
# #   4 4 4 4 
# #     3 3 3 
# #       2 2 
# #         1 
# for i in range(5,0,-1):
#     for s in range(5-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(i,end=" ")
#     print()

# # =========================================
# #         1 
# #       2 2 2 
# #     3 3 3 3 3 
# #   4 4 4 4 4 4 4 
# # 5 5 5 5 5 5 5 5 5
# for i in range(1,6,1):
#     for s in range(5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1,1):
#         print(i,end=" ")
#     for k in range(1,i,1):
#         print(i,end=" ")
#     print()

# # =========================================
# # 5 5 5 5 5 5 5 5 5 
# #   4 4 4 4 4 4 4 
# #     3 3 3 3 3 
# #       2 2 2 
# #         1 
# for i in range(5,0,-1):
#     for s in range(5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1,1):
#         print(i,end=" ")
#     for k in range(1,i,1):
#         print(i,end=" ")
#     print()


# # =========================================
# #         5 
# #       4 4 4 
# #     3 3 3 3 3 
# #   2 2 2 2 2 2 2 
# # 1 1 1 1 1 1 1 1 1 
# for i in range(5,0,-1):
#     for s in range(i-1):
#         print(" ",end=" ")
#     for j in range(i,6,1):
#         print(i,end=" ")
#     for k in range(5-i):
#         print(i,end=" ")
#     print()



# # ===========================================
# # 1 1 1 1 1 1 1 1 1 
# #   2 2 2 2 2 2 2 
# #     3 3 3 3 3 
# #       4 4 4 
# #         5 
# for i in range(1,6,1):
#     for s in range(1,i,1):
#         print(" ",end=" ")
#     for j in range(6-i):
#         print(i,end=" ")
#     for k in range(5-i):
#         print(i,end=" ")
#     print()



# # ===========================================
# #         5 
# #       5 4 5 
# #     5 4 3 4 5 
# #   5 4 3 2 3 4 5 
# # 5 4 3 2 1 2 3 4 5 
# for i in range(5,0,-1):
#     for s in range(4,5-i,-1):
#         print(" ",end=" ")
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     for k in range(i+1,6,1):
#         print(k,end=" ")
#     print()


# # ===========================================
# # 5 4 3 2 1 2 3 4 5 
# #   5 4 3 2 3 4 5 
# #     5 4 3 4 5 
# #       5 4 5 
# #         5 
# for i in range(1,6,1):
#     for s in range(1,i,1):
#         print(" ",end=" ")
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     for k in range(i+1,6,1):
#         print(k,end=" ")
#     print()

# # =============================================
# # 1 2 3 4 5 4 3 2 1 
# #   1 2 3 4 3 2 1 
# #     1 2 3 2 1 
# #       1 2 1 
# #         1 
# for i in range(5,0,-1):
#     for s in range(5,i,-1):
#         print(" ",end=" ")
#     for j in range(1,i+1,1):
#         print(j,end=" ")
#     for k in range(i-1,0,-1):
#         print(k,end=" ")
#     print()


# # ============================================
# # 5 4 3 2 1 2 3 4 5 
# #   4 3 2 1 2 3 4 
# #     3 2 1 2 3 
# #       2 1 2 
# #         1 
# for i in range(5,0,-1):
#     for s in range(5,i,-1):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     for k in range(2,i+1,1):
#         print(k,end=" ")
#     print()



# # =========================================
# # 1 2 3 4 5 4 3 2 1 
# #   2 3 4 5 4 3 2 
# #     3 4 5 4 3 
# #       4 5 4 
# #         5 
# for i in range(1,6,1):
#     for s in range(1,i,1):
#         print(" ",end=" ")
#     for j in range(i,6,1):
#         print(j,end=" ")
#     for k in range(4,i-1,-1):
#         print(k,end=" ")
#     print()


# =============================================
#         1 
#       1 2 1 
#     1 2 3 2 1 
#   1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1 
# for i in range(1,6,1):
#     for s in range(5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1,1):
#         print(j,end=" ")
#     for k in range(i-1,0,-1):
#         print(k,end=" ")
#     print()

# =============================================
# 1 2 3 4 5 4 3 2 1
#   1 2 3 4 3 2 1
#     1 2 3 2 1
#       1 2 1
#         1 
# for i in range(5,0,-1):
#     for s in range(5,i,-1):
#         print(" ",end=" ")
#     for j in range(1,i+1,1):
#         print(j,end=" ")
#     for k in range(i-1,0,-1):
#         print(k,end=" ")
#     print()

# ==============================================
# * * * * * 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# for i in range(1,6,1):
#     for j in range(1,6,1):
#         if i==1:
#             print("*",end=" ")
#         else:
#             print(j,end=" ")
#     print()

# ===============================================
# * * * * * 
# 1 2 3 4 5 
# * * * * * 
# 1 2 3 4 5 
# * * * * * 
# for i in range(1,6,1):
#     for j in range(1,6,1):
#         if i%2!=0:
#             print("*",end=" ")
#         else:
#             print(j,end=" ")
#     print()

# ===================================================
# * 2 * 4 * 
# * 2 * 4 * 
# * 2 * 4 * 
# * 2 * 4 * 
# * 2 * 4 * 
# for i in range(1,6,1):
#     for j in range(1,6,1):
#         if j%2!=0:
#             print("*",end=" ")
#         else:
#             print(j,end=" ")
#     print()

# ======================================
# *   *   * 
# *   *   * 
# *   *   * 
# *   *   * 
# *   *   * 
# for i in range(1,6,1):
#     for j in range(1,6,1):
#         if j%2!=0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# =============================================
#     *     
#     *     
# * * * * * 
#     *     
#     *   
# for i in range(1,6,1):
#     for j in range(1,6,1):
#         if i==3 or j==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# * * * * * * * 
# *           * 
# *           * 
# *           * 
# *           * 
# *           * 
# * * * * * * * 
# for i in range(1,8,1):
#     for j in range(1,8,1):
#         if i==1 or i==7 or j==1 or j==7:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# =======================================================
# * * * * * * * 
# *     *     * 
# *     *     * 
# * * * * * * * 
# *     *     * 
# *     *     * 
# * * * * * * * 
# for i in range(1,8,1):
#     for j in range(1,8,1):
#         if i==1 or i==7 or i==4 or j==1 or j==7 or j==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# ===========================================================
# * * * *     * 
#       *     * 
#       *     * 
# * * * * * * * 
# *     *       
# *     *       
# *     * * * * 
# for i in range(1,8,1):
#     for j in range(1,8,1):
#         if j==4 or i==1 and j<=4 or i==7 and j>=4 or j==7 and i<=4 or i==4 or j==1 and i>=4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# *         
#   *       
#     *     
#       *   
#         * 
# for i in range(1,6,1):
#     for j in range(1,6,1):
#         if i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#         * 
#       *   
#     *     
#   *       
# *   
# for i in range(1,6,1):
#     for j in range(5,0,-1):
#         if i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ===============================================================================
# * * * * * * * * * * * 
# * *       *     *   * 
# *   *     *   *     * 
# *     *   * *       * 
# *       * *         * 
# * * * * * * * * * * * 
# *     *   * *       * 
# *   *     *   *     * 
# * *       *     *   * 
# *         *       * * 
# * * * * * * * * * * * 
# for i in range(1,12,1):
#     for j in range(1,12,1):
#         if i==1 or i==11 or j==1 or j==11 or i+j==11 or i==j or j==6 or i==6:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ================================================
# *           * 
#   *       *   
#     *   *     
#       *       
#       *       
#       *       
#       *  
# for i in range(1,8,1):
#     for j in range(1,8,1):
#         if i==j and i<=4 or i+j==8 and i<=4 or j==4 and i>=4 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ==============================
#           *           
#         *   *         
# * * * * * * * * * * * 
#   * *           * *   
#   * *           * *   
# * * * * * * * * * * * 
#         *   *         
#           *
for i in range(1,9,1):
    for j in range(1,12,1):
        if i==3 or i==6 or i+j==7 or i+j==14 or j-i==5 or i-j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# ==================================
# *                 * 
# * *             * * 
# * * *         * * * 
# * * * *     * * * * 
# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 * 
# for i in range(1,6,1):
#     for j in range(1,i+1,1):
#         print('*',end=" ")
#     for s in range(2*(5-i)):
#          print(' ',end=" ")
#     for k in range(1,i+1,1):
#             print('*',end=" ")
#     print()
# for i in range(1,5,1):
#     for j in range(1,6-i,1):
#         print('*',end=" ")
#     for s in range(2*(i)):
#          print(' ',end=" ")
#     for k in range(1,6-i,1):
#             print('*',end=" ")
#     print()

# =========================================================
# *     * 
# *   *   
# * *     
# *       
# * *     
# *   *   
# *     * 
# for i in range(1,8,1):
#     for j in range(1,5,1):
#         if j==1 or i+j==5 or i-j==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
