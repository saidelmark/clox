#ifndef CLOX_VM_H
#define CLOX_VM_H

#include "chunk.h"
#include "value.h"

#define STACK_MAX 256

typedef struct {
  Chunk* chunk;
  uint8_t* ip;
  Value stack[STACK_MAX];
  Value* stackTop;
} VM;

typedef enum {
  INTERPRET_OK,
  INTERPRET_COMPILE_ERROR,
  INTERPRET_RUNTEMI_ERROR,
} InterpretResults;

void initVM();
void freeVM();
InterpretResults interpret(Chunk* chunk);

void push(Value value);
Value pop();

#endif
