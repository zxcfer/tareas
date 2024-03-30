package controller

import (
	"firego/auth"

	"github.com/gin-gonic/gin"
)

// AuthController is the controller for handling authentication requests
type AuthController struct {
	authService *auth.AuthService
}

func NewAuthController(authService *auth.AuthService) *AuthController {
	return &AuthController{authService}
}

func (c *AuthController) Login(ctx *gin.Context) {
	// Get the email and password from the request body
	var registrationData struct {
		Email    string `json:"email"`
		Password string `json:"password"`
	}

	if err := ctx.ShouldBindJSON(&registrationData); err != nil {
		ctx.AbortWithStatusJSON(400, gin.H{"error": "Invalid request body"})
		return
	}

	if registrationData.Email == "" || registrationData.Password == "" {
		ctx.AbortWithStatusJSON(400, gin.H{"error": "Email and password are required"})
		return
	}

	// Register the new user and get a custom token for the user
	customToken, err := c.authService.Login(registrationData.Email, registrationData.Password)
	if err != nil {
		ctx.AbortWithStatusJSON(400, gin.H{"error": err.Error()})
		return
	}

	// Return the custom token to the client
	ctx.JSON(200, gin.H{"token": customToken})
}

// Register handles the POST /register route and creates a new user with the provided credentials
func (c *AuthController) Register(ctx *gin.Context) {
	// Get the email and password from the request body
	var registrationData struct {
		Email    string `json:"email"`
		Password string `json:"password"`
	}

	if err := ctx.ShouldBindJSON(&registrationData); err != nil {
		ctx.AbortWithStatusJSON(400, gin.H{"error": "Invalid request body"})
		return
	}

	if registrationData.Email == "" || registrationData.Password == "" {
		ctx.AbortWithStatusJSON(400, gin.H{"error": "Email and password are required"})
		return
	}

	// Register the new user and get a custom token for the user
	customToken, err := c.authService.Register(registrationData.Email, registrationData.Password)
	if err != nil {
		ctx.AbortWithStatusJSON(400, gin.H{"error": err.Error()})
		return
	}

	// Return the custom token to the client
	ctx.JSON(200, gin.H{"token": customToken})
}
